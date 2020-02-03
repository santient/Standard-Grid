#!/bin/sh
run_grid_instance (){
	python  ../../../../ml_root/ml_code_json.py  --bs 64 --lr_net 0.0001 --epochs 100000000000 --STANDARDGRID_root aa63f65af9fa3a606abc7a1274343a6d9f683c79863218ef1e2820b67a6c81914500924e4974a70f43d069621006a42f5dcbf84241e6c30b1c0af965ca6537ba --STANDARDGRID_hex e438a7bee4e6a05fc33a8c48924e80306329dc151d657f5dfa62406688b9f4d3ad2904014137ce6b4568b77e78467d9ce9be4e2815f8b2d5884a5687fb70ca7b 
 	echo $? > STANDARDGRID_instance_output
}
run_grid_instance