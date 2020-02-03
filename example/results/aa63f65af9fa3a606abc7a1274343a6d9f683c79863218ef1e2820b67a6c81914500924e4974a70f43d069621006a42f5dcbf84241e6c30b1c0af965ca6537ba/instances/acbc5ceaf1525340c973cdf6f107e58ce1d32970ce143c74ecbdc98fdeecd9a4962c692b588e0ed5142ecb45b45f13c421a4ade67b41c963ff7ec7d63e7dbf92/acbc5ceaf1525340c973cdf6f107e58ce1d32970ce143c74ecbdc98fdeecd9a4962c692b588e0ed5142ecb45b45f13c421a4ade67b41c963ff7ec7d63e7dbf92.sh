#!/bin/sh
run_grid_instance (){
	python  ../../../../ml_root/ml_code_json.py  --bs 32 --lr_net 0.0001 --epochs 5000 --STANDARDGRID_root aa63f65af9fa3a606abc7a1274343a6d9f683c79863218ef1e2820b67a6c81914500924e4974a70f43d069621006a42f5dcbf84241e6c30b1c0af965ca6537ba --STANDARDGRID_hex acbc5ceaf1525340c973cdf6f107e58ce1d32970ce143c74ecbdc98fdeecd9a4962c692b588e0ed5142ecb45b45f13c421a4ade67b41c963ff7ec7d63e7dbf92 
 	echo $? > STANDARDGRID_instance_output
}
run_grid_instance