#!/bin/sh
run_grid_instance (){
	python  ../../../../ml_root/ml_code_json.py  --bs 32 --lr_net 0.01 --epochs 5000 --STANDARDGRID_root aa63f65af9fa3a606abc7a1274343a6d9f683c79863218ef1e2820b67a6c81914500924e4974a70f43d069621006a42f5dcbf84241e6c30b1c0af965ca6537ba --STANDARDGRID_hex dec9e9c02273b8f653bf86e3c1fcc484c058901b94548c55e637e033180a51bb574b2e51c14e1fdbbeef4278331fbcb1703c55114f637ce9712afe977d717076 
 	echo $? > STANDARDGRID_instance_output
}
run_grid_instance