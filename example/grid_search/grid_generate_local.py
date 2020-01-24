import simple_grid
import os

if __name__=="__main__":

	grid=simple_grid.Grid(central_command_parallel=False)

	grid.register('bs', [32,64])
	grid.register('lr_net', [0.001,0.0001])
	grid.register('epochs', [5000])

	grid.generate()
	grid_local_command_prefix="python %s"%os.path.abspath("../ml_root/ml_code.py")
	grid_central_command_prefix="sh"
	grid.operationalize("%s"%os.path.abspath("../results/"),grid_local_command_prefix,grid_central_command_prefix)
