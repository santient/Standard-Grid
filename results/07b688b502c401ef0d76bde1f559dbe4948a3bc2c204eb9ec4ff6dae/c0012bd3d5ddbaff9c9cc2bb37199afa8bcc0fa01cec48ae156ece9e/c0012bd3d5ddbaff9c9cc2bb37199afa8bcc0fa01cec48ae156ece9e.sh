#!/bin/sh
run_grid_instance (){
	sh  --bs 32 --lr_net 0.0001 --epochs 100000000000 --CMUGRID_root ../../results/07b688b502c401ef0d76bde1f559dbe4948a3bc2c204eb9ec4ff6dae/c0012bd3d5ddbaff9c9cc2bb37199afa8bcc0fa01cec48ae156ece9e --CMUGRID_hex c0012bd3d5ddbaff9c9cc2bb37199afa8bcc0fa01cec48ae156ece9e 
 	echo "Exit code" $? > ../../results/07b688b502c401ef0d76bde1f559dbe4948a3bc2c204eb9ec4ff6dae/c0012bd3d5ddbaff9c9cc2bb37199afa8bcc0fa01cec48ae156ece9e/CMUGRID_instance_output
}
run_grid_instance