#!/bin/sh
run_grid_instance (){
	python  ../../../../ml_root/ml_code_json.py  --bs 64 --lr_net 0.01 --epochs 5000 --STANDARDGRID_root aa63f65af9fa3a606abc7a1274343a6d9f683c79863218ef1e2820b67a6c81914500924e4974a70f43d069621006a42f5dcbf84241e6c30b1c0af965ca6537ba --STANDARDGRID_hex 707634933f83f89c2bc862e033d1858ebda3acc9add87041da05c060e96d0d1203ff825d9e9d6a88fb6ec19f9e31eb12029d0ed8a652afe4609ee9d4b717eecf 
 	echo $? > STANDARDGRID_instance_output
}
run_grid_instance