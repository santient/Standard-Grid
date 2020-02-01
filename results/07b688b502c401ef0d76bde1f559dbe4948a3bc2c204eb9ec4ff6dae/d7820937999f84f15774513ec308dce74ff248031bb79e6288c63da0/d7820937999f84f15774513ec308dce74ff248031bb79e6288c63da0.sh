#!/bin/sh
run_grid_instance (){
	sh  --bs 64 --lr_net 0.001 --epochs 100000000000 --CMUGRID_root ../../results/07b688b502c401ef0d76bde1f559dbe4948a3bc2c204eb9ec4ff6dae/d7820937999f84f15774513ec308dce74ff248031bb79e6288c63da0 --CMUGRID_hex d7820937999f84f15774513ec308dce74ff248031bb79e6288c63da0 
 	echo "Exit code" $? > ../../results/07b688b502c401ef0d76bde1f559dbe4948a3bc2c204eb9ec4ff6dae/d7820937999f84f15774513ec308dce74ff248031bb79e6288c63da0/CMUGRID_instance_output
}
run_grid_instance