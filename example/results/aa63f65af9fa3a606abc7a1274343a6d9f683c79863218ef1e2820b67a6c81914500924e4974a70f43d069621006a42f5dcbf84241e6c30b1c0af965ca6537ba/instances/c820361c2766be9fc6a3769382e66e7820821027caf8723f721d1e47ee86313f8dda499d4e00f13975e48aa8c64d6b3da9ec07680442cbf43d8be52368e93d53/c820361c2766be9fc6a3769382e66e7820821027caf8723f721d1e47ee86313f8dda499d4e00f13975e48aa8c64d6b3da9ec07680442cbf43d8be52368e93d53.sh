#!/bin/sh
run_grid_instance (){
	python  ../../../../ml_root/ml_code_json.py  --bs 64 --lr_net 0.001 --epochs 6000 --STANDARDGRID_root aa63f65af9fa3a606abc7a1274343a6d9f683c79863218ef1e2820b67a6c81914500924e4974a70f43d069621006a42f5dcbf84241e6c30b1c0af965ca6537ba --STANDARDGRID_hex c820361c2766be9fc6a3769382e66e7820821027caf8723f721d1e47ee86313f8dda499d4e00f13975e48aa8c64d6b3da9ec07680442cbf43d8be52368e93d53 
 	echo $? > STANDARDGRID_instance_output
}
run_grid_instance