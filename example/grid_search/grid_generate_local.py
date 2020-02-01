import simple_grid
import time
import os

if __name__=="__main__":

	grid=simple_grid.Grid("../ml_root/ml_code.py","../results/")

	grid.register('bs', [32,64])
	grid.register('lr_net', [0.001,0.0001])
	grid.register('epochs', [5000,100000000000])

	grid.generate_grid()
	grid_local_command_prefix="sh"
	grid_local_command_postfix=""

	grid.generate_shell_instances(prefix="python ",postfix="")
#	grid.create_runner()
	grid.create_runner(num_runners=3,runners_prefix=["sh","sh","sh"])


#	#%os.path.abspath("../ml_root/ml_code.py")
#	grid_central_command_prefix="sh"
#	grid_central_command_postfix=""
#
#
#	grid_runner_command_prefix="python %s"
#	grid_runner_command_postfix=""
#
#	grid.operationalize(grid_central_command_prefix,grid_central_command_postfix,grid_local_command_prefix, grid_local_command_postfix, grid_runner_command_prefix, grid_runner_command_postfix)

