#!/bin/sh
run_grid_instance (){
	python  ../../../../ml_root/ml_code_json.py  --bs 64 --lr_net 0.0001 --epochs 6000 --STANDARDGRID_root aa63f65af9fa3a606abc7a1274343a6d9f683c79863218ef1e2820b67a6c81914500924e4974a70f43d069621006a42f5dcbf84241e6c30b1c0af965ca6537ba --STANDARDGRID_hex 8f690fcc3748a8da7e341d0570c335638defd336e00894e756be51988bde15e750be2fe3049877808246f8c3c6d44102b631240c16705ebbaf5ee369f4a45cad 
 	echo $? > STANDARDGRID_instance_output
}
run_grid_instance