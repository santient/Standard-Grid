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

Create a folder within the 
