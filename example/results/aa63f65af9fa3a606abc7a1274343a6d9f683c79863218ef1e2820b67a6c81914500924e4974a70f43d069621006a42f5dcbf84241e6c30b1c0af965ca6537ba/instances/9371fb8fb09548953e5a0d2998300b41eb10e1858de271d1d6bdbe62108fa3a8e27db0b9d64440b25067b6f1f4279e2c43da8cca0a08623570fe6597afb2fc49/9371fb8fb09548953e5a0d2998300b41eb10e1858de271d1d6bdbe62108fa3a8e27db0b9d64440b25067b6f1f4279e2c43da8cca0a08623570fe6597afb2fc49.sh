#!/bin/sh
run_grid_instance (){
	python  ../../../../ml_root/ml_code_json.py  --bs 32 --lr_net 0.01 --epochs 6000 --STANDARDGRID_root aa63f65af9fa3a606abc7a1274343a6d9f683c79863218ef1e2820b67a6c81914500924e4974a70f43d069621006a42f5dcbf84241e6c30b1c0af965ca6537ba --STANDARDGRID_hex 9371fb8fb09548953e5a0d2998300b41eb10e1858de271d1d6bdbe62108fa3a8e27db0b9d64440b25067b6f1f4279e2c43da8cca0a08623570fe6597afb2fc49 
 	echo $? > STANDARDGRID_instance_output
}
run_grid_instance