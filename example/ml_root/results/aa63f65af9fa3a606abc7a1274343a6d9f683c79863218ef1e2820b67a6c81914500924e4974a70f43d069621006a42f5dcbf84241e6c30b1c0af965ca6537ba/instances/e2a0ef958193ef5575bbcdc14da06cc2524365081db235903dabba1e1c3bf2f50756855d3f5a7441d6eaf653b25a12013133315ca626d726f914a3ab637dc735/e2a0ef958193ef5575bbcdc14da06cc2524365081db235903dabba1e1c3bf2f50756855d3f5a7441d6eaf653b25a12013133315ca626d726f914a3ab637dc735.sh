#!/bin/sh
run_grid_instance (){
	python  ../../../../ml_code_json.py  --bs 64 --lr_net 0.001 --epochs 100000000000 
 	echo $? > STANDARDGRID_instance_output
}
run_grid_instance