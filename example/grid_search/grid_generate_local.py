import simple_grid
import os

if __name__=="__main__":

	grid=simple_grid.Grid()

	grid.register('bs', [32,64])
	grid.register('lr_net', [0.001,0.0001])
	grid.register('epochs', [5000,100000000000])

	grid.generate()
	#%os.path.abspath("../ml_root/ml_code.py")
	grid_central_command_prefix="sh"
	grid_central_command_postfix=""

	grid_local_command_prefix="sh"
	grid_local_command_postfix=""

	grid_runner_command_prefix="python %s"
	grid_runner_command_postfix=""

	grid.operationalize("../ml_root/ml_code.py","../results/",grid_central_command_prefix,grid_central_command_postfix,grid_local_command_prefix, grid_local_command_postfix, grid_runner_command_prefix, grid_runner_command_postfix)

