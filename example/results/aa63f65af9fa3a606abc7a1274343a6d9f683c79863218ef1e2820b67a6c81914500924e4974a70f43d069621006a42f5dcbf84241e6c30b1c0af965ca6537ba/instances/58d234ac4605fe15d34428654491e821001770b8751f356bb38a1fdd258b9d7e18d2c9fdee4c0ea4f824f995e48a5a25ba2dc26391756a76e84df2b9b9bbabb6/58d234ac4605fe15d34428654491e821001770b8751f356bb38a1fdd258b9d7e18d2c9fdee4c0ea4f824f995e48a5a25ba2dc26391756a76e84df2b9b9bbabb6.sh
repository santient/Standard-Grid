#!/bin/sh
run_grid_instance (){
	python  ../../../../ml_root/ml_code_json.py  --bs 64 --lr_net 0.0001 --epochs 5000 --STANDARDGRID_root aa63f65af9fa3a606abc7a1274343a6d9f683c79863218ef1e2820b67a6c81914500924e4974a70f43d069621006a42f5dcbf84241e6c30b1c0af965ca6537ba --STANDARDGRID_hex 58d234ac4605fe15d34428654491e821001770b8751f356bb38a1fdd258b9d7e18d2c9fdee4c0ea4f824f995e48a5a25ba2dc26391756a76e84df2b9b9bbabb6 
 	echo $? > STANDARDGRID_instance_output
}
run_grid_instance