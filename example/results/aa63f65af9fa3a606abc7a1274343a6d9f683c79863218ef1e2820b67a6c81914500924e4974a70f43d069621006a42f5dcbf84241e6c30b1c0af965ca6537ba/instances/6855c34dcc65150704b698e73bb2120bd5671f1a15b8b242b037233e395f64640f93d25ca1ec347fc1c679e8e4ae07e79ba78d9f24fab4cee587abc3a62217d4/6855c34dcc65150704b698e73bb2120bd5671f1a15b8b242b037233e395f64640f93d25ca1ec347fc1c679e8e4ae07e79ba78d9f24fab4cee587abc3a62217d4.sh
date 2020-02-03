#!/bin/sh
run_grid_instance (){
	python  ../../../../ml_root/ml_code_json.py  --bs 32 --lr_net 0.001 --epochs 100000000000 --STANDARDGRID_root aa63f65af9fa3a606abc7a1274343a6d9f683c79863218ef1e2820b67a6c81914500924e4974a70f43d069621006a42f5dcbf84241e6c30b1c0af965ca6537ba --STANDARDGRID_hex 6855c34dcc65150704b698e73bb2120bd5671f1a15b8b242b037233e395f64640f93d25ca1ec347fc1c679e8e4ae07e79ba78d9f24fab4cee587abc3a62217d4 
 	echo $? > STANDARDGRID_instance_output
}
run_grid_instance