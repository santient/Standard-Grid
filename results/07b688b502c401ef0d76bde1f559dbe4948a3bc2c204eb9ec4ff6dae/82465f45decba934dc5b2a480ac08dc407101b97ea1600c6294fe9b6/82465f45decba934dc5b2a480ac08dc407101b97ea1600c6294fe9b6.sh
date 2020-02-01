#!/bin/sh
run_grid_instance (){
	sh  --bs 32 --lr_net 0.001 --epochs 5000 --CMUGRID_root ../../results/07b688b502c401ef0d76bde1f559dbe4948a3bc2c204eb9ec4ff6dae/82465f45decba934dc5b2a480ac08dc407101b97ea1600c6294fe9b6 --CMUGRID_hex 82465f45decba934dc5b2a480ac08dc407101b97ea1600c6294fe9b6 
 	echo "Exit code" $? > ../../results/07b688b502c401ef0d76bde1f559dbe4948a3bc2c204eb9ec4ff6dae/82465f45decba934dc5b2a480ac08dc407101b97ea1600c6294fe9b6/CMUGRID_instance_output
}
run_grid_instance