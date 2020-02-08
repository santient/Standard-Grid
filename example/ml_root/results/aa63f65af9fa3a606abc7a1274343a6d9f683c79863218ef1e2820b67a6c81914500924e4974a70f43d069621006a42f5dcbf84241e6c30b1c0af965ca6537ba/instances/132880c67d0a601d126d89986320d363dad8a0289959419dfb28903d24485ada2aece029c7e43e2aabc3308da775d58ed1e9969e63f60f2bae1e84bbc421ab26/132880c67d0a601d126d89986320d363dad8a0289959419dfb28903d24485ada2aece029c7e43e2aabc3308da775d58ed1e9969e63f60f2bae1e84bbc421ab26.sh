#!/bin/sh
run_grid_instance (){
	python  ../../../../ml_code_json.py  --bs 32 --lr_net 0.01 --epochs 6000 
 	echo $? > STANDARDGRID_instance_output
}
run_grid_instance