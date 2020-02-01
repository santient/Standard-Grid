#!/bin/sh
run_grid_instance (){
	python  ../../../../ml_root/ml_code.py  --bs 64 --lr_net 0.0001 --epochs 100000000000 --STANDARDGRID_root 2525fdbb54fcdf20e68567f24652da350868ad5d148c542769a8c473cc7a74d1b83e64baa57f84be835e148f9a2879005cda6e34f88d6c2b83050dc26424ff4b --STANDARDGRID_hex 507350a794daef43238421802e1caaad3fade80bd5d931151f8894b8d23a21ffb1e1ed00d6d880db77fe282b84d7cb0730a5615380985653744d1298270bfa18 
 	echo "Exit code" $? > STANDARDGRID_instance_output
}
run_grid_instance