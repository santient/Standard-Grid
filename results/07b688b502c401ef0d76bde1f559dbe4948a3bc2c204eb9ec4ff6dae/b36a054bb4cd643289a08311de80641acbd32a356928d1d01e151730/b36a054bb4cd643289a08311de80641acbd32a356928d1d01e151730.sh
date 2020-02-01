#!/bin/sh
run_grid_instance (){
	sh  --bs 64 --lr_net 0.0001 --epochs 100000000000 --CMUGRID_root ../../results/07b688b502c401ef0d76bde1f559dbe4948a3bc2c204eb9ec4ff6dae/b36a054bb4cd643289a08311de80641acbd32a356928d1d01e151730 --CMUGRID_hex b36a054bb4cd643289a08311de80641acbd32a356928d1d01e151730 
 	echo "Exit code" $? > ../../results/07b688b502c401ef0d76bde1f559dbe4948a3bc2c204eb9ec4ff6dae/b36a054bb4cd643289a08311de80641acbd32a356928d1d01e151730/CMUGRID_instance_output
}
run_grid_instance