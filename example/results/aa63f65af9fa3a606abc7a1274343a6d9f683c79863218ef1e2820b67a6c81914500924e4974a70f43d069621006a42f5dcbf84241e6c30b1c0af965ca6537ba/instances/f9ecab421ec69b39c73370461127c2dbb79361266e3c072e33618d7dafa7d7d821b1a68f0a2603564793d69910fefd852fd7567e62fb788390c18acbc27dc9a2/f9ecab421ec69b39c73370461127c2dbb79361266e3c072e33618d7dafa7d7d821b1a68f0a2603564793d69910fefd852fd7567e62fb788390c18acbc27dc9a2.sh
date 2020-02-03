#!/bin/sh
run_grid_instance (){
	python  ../../../../ml_root/ml_code_json.py  --bs 64 --lr_net 0.001 --epochs 100000000000 --STANDARDGRID_root aa63f65af9fa3a606abc7a1274343a6d9f683c79863218ef1e2820b67a6c81914500924e4974a70f43d069621006a42f5dcbf84241e6c30b1c0af965ca6537ba --STANDARDGRID_hex f9ecab421ec69b39c73370461127c2dbb79361266e3c072e33618d7dafa7d7d821b1a68f0a2603564793d69910fefd852fd7567e62fb788390c18acbc27dc9a2 
 	echo $? > STANDARDGRID_instance_output
}
run_grid_instance