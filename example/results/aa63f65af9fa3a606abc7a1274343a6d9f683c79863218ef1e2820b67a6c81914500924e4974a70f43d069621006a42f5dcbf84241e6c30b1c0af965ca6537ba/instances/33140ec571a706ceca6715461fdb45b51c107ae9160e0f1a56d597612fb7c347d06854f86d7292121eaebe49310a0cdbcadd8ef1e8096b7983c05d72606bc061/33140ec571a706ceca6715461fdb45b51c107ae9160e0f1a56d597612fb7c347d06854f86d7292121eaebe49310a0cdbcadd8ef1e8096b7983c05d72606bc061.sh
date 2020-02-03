#!/bin/sh
run_grid_instance (){
	python  ../../../../ml_root/ml_code_json.py  --bs 64 --lr_net 0.001 --epochs 5000 --STANDARDGRID_root aa63f65af9fa3a606abc7a1274343a6d9f683c79863218ef1e2820b67a6c81914500924e4974a70f43d069621006a42f5dcbf84241e6c30b1c0af965ca6537ba --STANDARDGRID_hex 33140ec571a706ceca6715461fdb45b51c107ae9160e0f1a56d597612fb7c347d06854f86d7292121eaebe49310a0cdbcadd8ef1e8096b7983c05d72606bc061 
 	echo $? > STANDARDGRID_instance_output
}
run_grid_instance