#!/bin/sh
run_grid_instance (){
	python  ../../../../ml_root/ml_code_json.py  --bs 32 --lr_net 0.001 --epochs 5000 --STANDARDGRID_root aa63f65af9fa3a606abc7a1274343a6d9f683c79863218ef1e2820b67a6c81914500924e4974a70f43d069621006a42f5dcbf84241e6c30b1c0af965ca6537ba --STANDARDGRID_hex 100781d28d0351d2ce09cee5f3e0d975432fc549282704330505e7eafad5446a9c4e8fc0935fb4712fcd91921bc7472bf629337a99dac8c63e4f7a53b006c1fe 
 	echo $? > STANDARDGRID_instance_output
}
run_grid_instance