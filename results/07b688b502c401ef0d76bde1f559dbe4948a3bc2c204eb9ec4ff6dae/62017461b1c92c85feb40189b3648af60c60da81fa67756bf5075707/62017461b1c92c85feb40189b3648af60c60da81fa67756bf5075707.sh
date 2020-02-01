#!/bin/sh
run_grid_instance (){
	sh  --bs 64 --lr_net 0.001 --epochs 5000 --CMUGRID_root ../../results/07b688b502c401ef0d76bde1f559dbe4948a3bc2c204eb9ec4ff6dae/62017461b1c92c85feb40189b3648af60c60da81fa67756bf5075707 --CMUGRID_hex 62017461b1c92c85feb40189b3648af60c60da81fa67756bf5075707 
 	echo "Exit code" $? > ../../results/07b688b502c401ef0d76bde1f559dbe4948a3bc2c204eb9ec4ff6dae/62017461b1c92c85feb40189b3648af60c60da81fa67756bf5075707/CMUGRID_instance_output
}
run_grid_instance