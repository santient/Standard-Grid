#!/bin/sh
run_grid_instance (){
	python  ../../../../ml_root/ml_code_json.py  --bs 32 --lr_net 0.0001 --epochs 100000000000 --STANDARDGRID_root aa63f65af9fa3a606abc7a1274343a6d9f683c79863218ef1e2820b67a6c81914500924e4974a70f43d069621006a42f5dcbf84241e6c30b1c0af965ca6537ba --STANDARDGRID_hex 0aac44eee70bbd9d7e77fe2250a47872f8b29fbb2f1dead8df3829052b3ec198dcf27d70bb425b213ec9a2eb7b93b782325244d92c7ea8aee521080f59955ad9 
 	echo $? > STANDARDGRID_instance_output
}
run_grid_instance