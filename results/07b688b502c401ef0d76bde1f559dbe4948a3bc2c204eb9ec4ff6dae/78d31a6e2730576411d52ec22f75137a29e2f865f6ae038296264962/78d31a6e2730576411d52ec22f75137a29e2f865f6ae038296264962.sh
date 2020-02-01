#!/bin/sh
run_grid_instance (){
	sh  --bs 64 --lr_net 0.0001 --epochs 5000 --CMUGRID_root ../../results/07b688b502c401ef0d76bde1f559dbe4948a3bc2c204eb9ec4ff6dae/78d31a6e2730576411d52ec22f75137a29e2f865f6ae038296264962 --CMUGRID_hex 78d31a6e2730576411d52ec22f75137a29e2f865f6ae038296264962 
 	echo "Exit code" $? > ../../results/07b688b502c401ef0d76bde1f559dbe4948a3bc2c204eb9ec4ff6dae/78d31a6e2730576411d52ec22f75137a29e2f865f6ae038296264962/CMUGRID_instance_output
}
run_grid_instance