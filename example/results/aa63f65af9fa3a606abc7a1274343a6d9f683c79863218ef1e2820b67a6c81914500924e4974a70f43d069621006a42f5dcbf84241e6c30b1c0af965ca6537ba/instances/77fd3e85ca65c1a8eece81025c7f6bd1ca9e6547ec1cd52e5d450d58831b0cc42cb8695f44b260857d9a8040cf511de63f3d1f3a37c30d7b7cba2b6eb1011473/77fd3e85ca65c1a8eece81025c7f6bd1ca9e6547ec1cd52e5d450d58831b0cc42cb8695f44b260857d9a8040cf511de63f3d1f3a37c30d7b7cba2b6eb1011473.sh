#!/bin/sh
run_grid_instance (){
	python  ../../../../ml_root/ml_code_json.py  --bs 32 --lr_net 0.01 --epochs 100000000000 --STANDARDGRID_root aa63f65af9fa3a606abc7a1274343a6d9f683c79863218ef1e2820b67a6c81914500924e4974a70f43d069621006a42f5dcbf84241e6c30b1c0af965ca6537ba --STANDARDGRID_hex 77fd3e85ca65c1a8eece81025c7f6bd1ca9e6547ec1cd52e5d450d58831b0cc42cb8695f44b260857d9a8040cf511de63f3d1f3a37c30d7b7cba2b6eb1011473 
 	echo $? > STANDARDGRID_instance_output
}
run_grid_instance