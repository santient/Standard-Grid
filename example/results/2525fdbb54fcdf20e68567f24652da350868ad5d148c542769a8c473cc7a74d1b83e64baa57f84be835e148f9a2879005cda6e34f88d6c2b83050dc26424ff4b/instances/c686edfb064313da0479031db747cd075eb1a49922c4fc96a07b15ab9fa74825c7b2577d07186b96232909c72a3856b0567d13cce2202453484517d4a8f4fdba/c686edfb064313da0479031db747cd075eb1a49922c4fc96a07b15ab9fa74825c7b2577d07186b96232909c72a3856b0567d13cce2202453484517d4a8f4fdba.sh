#!/bin/sh
run_grid_instance (){
	python  ../../../../ml_root/ml_code.py  --bs 32 --lr_net 0.0001 --epochs 100000000000 --STANDARDGRID_root 2525fdbb54fcdf20e68567f24652da350868ad5d148c542769a8c473cc7a74d1b83e64baa57f84be835e148f9a2879005cda6e34f88d6c2b83050dc26424ff4b --STANDARDGRID_hex c686edfb064313da0479031db747cd075eb1a49922c4fc96a07b15ab9fa74825c7b2577d07186b96232909c72a3856b0567d13cce2202453484517d4a8f4fdba 
 	echo "Exit code" $? > STANDARDGRID_instance_output
}
run_grid_instance