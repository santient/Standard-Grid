#!/bin/sh
run_grid_instance (){
	python  ../../../../ml_root/ml_code.py  --bs 32 --lr_net 0.0001 --epochs 5000 --STANDARDGRID_root 2525fdbb54fcdf20e68567f24652da350868ad5d148c542769a8c473cc7a74d1b83e64baa57f84be835e148f9a2879005cda6e34f88d6c2b83050dc26424ff4b --STANDARDGRID_hex 48c00a5ae2dec514da875a2d6c34ab886a77bd078023ef4236360bc4ca5cf045d70c0e3fe8776fc9cb742b34a29ffef59fff7b5f4c608ada0dcb89f805e537af 
 	echo "Exit code" $? > STANDARDGRID_instance_output
}
run_grid_instance