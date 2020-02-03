#!/bin/sh
run_grid_instance (){
	python  ../../../../ml_root/ml_code_json.py  --bs 32 --lr_net 0.0001 --epochs 6000 --STANDARDGRID_root aa63f65af9fa3a606abc7a1274343a6d9f683c79863218ef1e2820b67a6c81914500924e4974a70f43d069621006a42f5dcbf84241e6c30b1c0af965ca6537ba --STANDARDGRID_hex 615a38af80f1c1b57e3ad5d2c250b69e6ce030963f20ad0cd17cf0c590593019028935837f6a44e40c642f948da2eb816279474d6aa766ab5d714f8c35577c64 
 	echo $? > STANDARDGRID_instance_output
}
run_grid_instance