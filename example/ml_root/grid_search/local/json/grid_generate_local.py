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
	#Breaks the work on 4 GPUs, runs 2 jobs on each gpu
	grid.create_runner(num_runners=4,runners_prefix=["CUDA_VISIBLE_DEVIDES=%d sh"%i for i in range(4)],parallel=2)

