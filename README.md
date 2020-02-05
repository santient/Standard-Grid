# Standard-Grid
Standard-Grid @ Standard-SDK: standard protocol for reporting grid search results for students advised by me.

# Preliminaries

Assume you have a code written in a particular language and library. Assume you have a workstation or a slurm-based cluster. Assume your code is under a directory called ml_root. This directory has two properties 1) it has the main entry point of your code, 2) no write operations outside this directory is made by your code.
We will call the entry point of your code as ml_code.x. In reality there are no requirements for python, c++ or any other language. ml_code.x takes commands from argv using stanard --command style of system arguments. 

Example:
```
python ml_code.py --lr 0.001 --dataset woopsi --bounding_boxes yolo66666.666 --openface_file closed_neck.wtf
```

Let's assume the above file writes some outputs (like experimenal outputs) to a directory called output inside ml_root. output can never be outside the ml_root. ml_code.x will create the directory if not existing. 

The above are not unreasonable assumptions. For example, if the results dir does not exist then your code will crash even if not going through a grid search.

Let's assume the results of the experiments are written into a depth-1 dictionary and then dumped as a json file within the output directory. Example of a simple code:

```python

import os
import time
import pickle
import standard_grid
import json

def get_arguments():
	parser = standard_grid.ArgParser()
	parser.register_parameter("--bs",int,32,"The batch size.")
	parser.register_parameter("--lr_net",float,0.001,"The learning rate of the model.")
	parser.register_parameter("--epochs",int,2000,"The number of epochs.")

	args=parser.compile_argparse()

	return args 


if __name__=="__main__":

	params=get_arguments()
	#The most complex ML model
	time.sleep(10)

	out_dir="output/"

	if not os.path.isdir(out_dir):
		os.makedirs(out_dir)

	results={"bestloss":.00123,"worst_loss":.0123}

	#this is important for the standard-grid, but not required.
	res_f=open(os.path.join(out_dir,"best.txt"),"w")
	res_f.write(json.dumps(results))

	#you can also write whatever you like to other places within the out_dir
	pickle.dump([0.001,0.00123,0.00321],open(os.path.join(out_dir,"weights.pkl"),"wb"))
```



# Grid Search

Create a folder within the ml_root for your grid search setup. let's call this grid_search. Then simply use an example similar to below. Call this grid_generate.py inside grid_search folder. ALWAYS run this code when active directory is in grid_search. 

```python
import standard_grid
import pickle
import time
import os

if __name__=="__main__":

	grid=standard_grid.Grid("../../../ml_code_json.py","../../../results/")

	grid.register('bs', [32,64])
	grid.register('lr_net', [0.001,0.01,0.0001])
	grid.register('epochs', [5000,6000,100000000000])

	grid.generate_grid()

	grid.generate_shell_instances(prefix="python ",postfix="")
```

First, you create a Grid object. The object takes two non-default arguments, one for where the entry point is and the second where you intend your grid searches to be stored at. I suggest creating one folder per project. This should also fall within ml_root. You can refer to these two folders relative or absolute. 

Second, you register the grid parameters. Subsequently, you call the generate_grid to create the combinations of your grid object. prefix and postfix are complex operations. Prefix can take arguments that are non-grid search. But mostly prefix and postfix will be as depicted above. After generate_shell_instances is called, no more parameters can be registered or the grid may not change. For each instance a hash depicted as $instance_hash is generated, and based on instnace hashes a $grid_hash is generated. Therefore identical grid searchers will results in similar hash. To run an identical grid multiple times, you can specify a unique id to the Grid constructor, which will be used to change the hash. 

Third, you call for the generate_shell_instnaces to create a shell instances for each combination. Each shell instance, will be created under results/$grid_hash/instances/$instance_hash/. These instances are the most important part of the Grid object. You can cd into results/$grid_hash/instances/$instance_hash/ and run $instance_hash to run the instance, but obviosuly this is too much work. Hence we create runners (next section).

The code above will save your grid in the active directory, which again should always be grid_search. The file name will be .$grid_hash.pkl. You can load the grid object afterwards using pickle. 

# Grid Runners

This is the part where the magic happens. We will just go by examples:

```python
	#Breaks the work on 4 GPUs, runs 2 jobs on each gpu
	grid.create_runner(num_runners=4,runners_prefix=["CUDA_VISIBLE_DEVIDES=%d sh"%i for i in range(4)],parallel=2)
```




