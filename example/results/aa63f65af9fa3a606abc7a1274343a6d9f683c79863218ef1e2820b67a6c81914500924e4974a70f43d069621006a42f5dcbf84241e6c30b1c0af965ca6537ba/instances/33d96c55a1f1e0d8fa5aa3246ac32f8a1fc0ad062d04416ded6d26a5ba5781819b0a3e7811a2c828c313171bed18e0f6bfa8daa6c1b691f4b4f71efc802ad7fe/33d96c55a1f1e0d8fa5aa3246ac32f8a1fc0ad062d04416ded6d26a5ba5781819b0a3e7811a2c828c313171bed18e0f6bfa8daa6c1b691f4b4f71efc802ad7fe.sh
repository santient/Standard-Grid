#!/bin/sh
run_grid_instance (){
	python  ../../../../ml_root/ml_code_json.py  --bs 64 --lr_net 0.01 --epochs 100000000000 --STANDARDGRID_root aa63f65af9fa3a606abc7a1274343a6d9f683c79863218ef1e2820b67a6c81914500924e4974a70f43d069621006a42f5dcbf84241e6c30b1c0af965ca6537ba --STANDARDGRID_hex 33d96c55a1f1e0d8fa5aa3246ac32f8a1fc0ad062d04416ded6d26a5ba5781819b0a3e7811a2c828c313171bed18e0f6bfa8daa6c1b691f4b4f71efc802ad7fe 
 	echo $? > STANDARDGRID_instance_output
}
run_grid_instance