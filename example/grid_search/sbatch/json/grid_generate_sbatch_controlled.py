import standard_grid
import time
import os

if __name__=="__main__":

	grid=standard_grid.Grid("../../../ml_root/ml_code_json.py","../../../results/")

	grid.register('bs', [32,64])
	grid.register('lr_net', [0.001,0.01,0.0001])
	grid.register('epochs', [5000,6000,100000000000])

	grid.generate_grid()
	grid_local_command_prefix="sh"
	grid_local_command_postfix=""

	grid.generate_shell_instances(prefix="python ",postfix="")
	total_at_a_time=8
	grid.create_runner(num_runners=total_at_a_time,runners_prefix=["sbatch -p gpu_low -c 1 -W"]*total_at_a_time)


