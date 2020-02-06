# Standard-Grid
Standard-Grid @ Standard-SDK: standard protocol for reporting grid search results for students advised by me.

# 1. Preliminaries

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



# 2. Grid Search

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

Third, you call for the generate_shell_instnaces to create a shell instances for each combination. Each shell instance, will be created under ml_root/results/$grid_hash/instances/$instance_hash/. These instances are the most important part of the Grid object. You can cd into ml_root/results/$grid_hash/instances/$instance_hash/ and run $instance_hash to run the instance, but obviosuly this is too much work. Hence we create runners (next section).

The code above will save your grid in the active directory, which again should always be grid_search. The file name will be .$grid_hash.pkl. You can load the grid object afterwards using pickle. 

# 3. Grid Runners

This is the part where the magic happens. We will just go by examples.

To break the job on 4 GPUs, run 2 jobs on each gpu until no more instances are present:

```python
	grid.create_runner(num_runners=4,runners_prefix=["CUDA_VISIBLE_DEVIDES=%d sh"%i for i in range(4)],parallel=2)
```

To run 8 sbatch jobs at a time until completion (make sure to run this from inside screen or dies after logout): 

```python
	total_at_a_time=8
	grid.create_runner(num_runners=total_at_a_time,runners_prefix=["sbatch -p gpu_low -c 1 --gres=gpu:1 -W"]*total_at_a_time)
```

To submit everything to the sbatch (you can log out regardless of screen or not - never submit in bulk using gpu_high unless permitted):

```python
	grid.create_runner(num_runners=None,runners_prefix=["sbatch -p gpu_low -c 1 --gres=gpu:1"])
```

Always make sure to check the squeue. After the creation of the grid runners, cd to ml_root/results/$grid_hash/central/attempt_x/ and run main.sh. This script needs to run from the folder it resides in. 

# 4. Grid Status and Resume

Change your active directory back to the grid_search. Remember any operations inside this directory needs to be called from within the directory itself. Load the .$grid_hash using pickle, and call:

```python
	grid.get_status()
```
This will tell you how many of your scripts ended successfully (status code 0), with error (status code !=0), still running (no status code), or not started yet (no status file). Status files are available in the ml_root/results/$grid_hash/instances/$instance_hash/STANDARDGRID_instance_output

To resume the grid using the operations which the .$grid_hash was pickled with, run the following (make sure the runner is created before the origin grid creation script is finished - essentially sections 2 and 3 are in one code, otherwise when the .$grid_hash is created, no runner is attached):

```python
grid.resume_as_before()
```
If you want to submit the ones which may already be running (sometimes atlas goes down, and everything that failed and was running needs to restart), specify hard_resume=True to above function.

Alternatively, you can copy the ml_root to some other machine and resume using:
```python
grid.resume( ... )
```
With arguments identical to create_runner function. 


# 4. Compile CSV

Remember when creating the json output, with non-nested results dictionary? Now we can get all the results in one go using:

```python
	grid.json_interpret("output/best.txt","interpretation.csv")
```

# Rermarks

1. Your mindset should be as if you are writing a code without caring for the grid search. Standard-Grid creates a grid search as an attachment for you. At not point a change is needed to ml_code.x, but rather simply following good code writing practices

2. Everything internally for Standard-Grid is relatively references. So moving your results directory and moving your ml_code.x will results in failure of grid search. Therefore, to begin with, solidify these two so you won't change them again. Also, grid_search folder could be the same when generating many different parameter sets, but does not need to be. You can have grid_search1,2,3, etc. However, good practice is to keep all your grid searches in the same place. So creation of grid is encouraged to be always in grid_search folder and grid destination to be results folder.
