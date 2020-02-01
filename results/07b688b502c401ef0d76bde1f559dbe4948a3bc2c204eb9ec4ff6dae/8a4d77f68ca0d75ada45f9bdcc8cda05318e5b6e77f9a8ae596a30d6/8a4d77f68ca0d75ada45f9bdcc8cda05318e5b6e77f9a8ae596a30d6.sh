#!/bin/sh
run_grid_instance (){
	sh  --bs 32 --lr_net 0.001 --epochs 100000000000 --CMUGRID_root ../../results/07b688b502c401ef0d76bde1f559dbe4948a3bc2c204eb9ec4ff6dae/8a4d77f68ca0d75ada45f9bdcc8cda05318e5b6e77f9a8ae596a30d6 --CMUGRID_hex 8a4d77f68ca0d75ada45f9bdcc8cda05318e5b6e77f9a8ae596a30d6 
 	echo "Exit code" $? > ../../results/07b688b502c401ef0d76bde1f559dbe4948a3bc2c204eb9ec4ff6dae/8a4d77f68ca0d75ada45f9bdcc8cda05318e5b6e77f9a8ae596a30d6/CMUGRID_instance_output
}
run_grid_instance