#!/bin/sh
run_grid_instance (){
	python  ../../../../ml_root/ml_code_json.py  --bs 64 --lr_net 0.01 --epochs 6000 --STANDARDGRID_root aa63f65af9fa3a606abc7a1274343a6d9f683c79863218ef1e2820b67a6c81914500924e4974a70f43d069621006a42f5dcbf84241e6c30b1c0af965ca6537ba --STANDARDGRID_hex 970b67d609b297dab3ba3d1a7dc25acfa1dc396f4e304361ef1009ea76d8b6238d73d037dc21d5871a284b154397aad7d8773e494f3562da60a7f42d45edef10 
 	echo $? > STANDARDGRID_instance_output
}
run_grid_instance