#!/bin/sh
run_grid_instance (){
	python  ../../../../ml_root/ml_code_json.py  --bs 32 --lr_net 0.001 --epochs 6000 --STANDARDGRID_root aa63f65af9fa3a606abc7a1274343a6d9f683c79863218ef1e2820b67a6c81914500924e4974a70f43d069621006a42f5dcbf84241e6c30b1c0af965ca6537ba --STANDARDGRID_hex 32b5ac8c4a3b7c906134da509eff0113aaafda4c442a95dec51a7d8d60705fd62de28ab8eb334e22929844039891a2952cd57473c704e2c4ee090ba491a836fc 
 	echo $? > STANDARDGRID_instance_output
}
run_grid_instance