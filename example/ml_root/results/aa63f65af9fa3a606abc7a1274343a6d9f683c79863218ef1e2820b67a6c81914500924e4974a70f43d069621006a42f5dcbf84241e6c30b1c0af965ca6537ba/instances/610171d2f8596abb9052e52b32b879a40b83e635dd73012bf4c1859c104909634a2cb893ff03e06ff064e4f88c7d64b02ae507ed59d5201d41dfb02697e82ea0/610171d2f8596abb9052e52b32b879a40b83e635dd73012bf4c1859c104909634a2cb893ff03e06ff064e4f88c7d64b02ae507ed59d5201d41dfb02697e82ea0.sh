#!/bin/sh
run_grid_instance (){
	python  ../../../../ml_code_json.py  --bs 32 --lr_net 0.0001 --epochs 5000 
 	echo $? > STANDARDGRID_instance_output
}
run_grid_instance