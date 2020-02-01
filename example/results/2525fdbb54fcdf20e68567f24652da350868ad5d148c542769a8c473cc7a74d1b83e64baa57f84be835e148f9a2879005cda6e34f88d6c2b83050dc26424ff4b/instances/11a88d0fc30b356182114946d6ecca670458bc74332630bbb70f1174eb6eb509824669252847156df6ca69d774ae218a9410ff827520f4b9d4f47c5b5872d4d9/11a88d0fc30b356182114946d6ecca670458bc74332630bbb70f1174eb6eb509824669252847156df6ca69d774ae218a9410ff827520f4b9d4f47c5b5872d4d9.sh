#!/bin/sh
run_grid_instance (){
	python  ../../../../ml_root/ml_code.py  --bs 32 --lr_net 0.001 --epochs 5000 --STANDARDGRID_root 2525fdbb54fcdf20e68567f24652da350868ad5d148c542769a8c473cc7a74d1b83e64baa57f84be835e148f9a2879005cda6e34f88d6c2b83050dc26424ff4b --STANDARDGRID_hex 11a88d0fc30b356182114946d6ecca670458bc74332630bbb70f1174eb6eb509824669252847156df6ca69d774ae218a9410ff827520f4b9d4f47c5b5872d4d9 
 	echo "Exit code" $? > STANDARDGRID_instance_output
}
run_grid_instance