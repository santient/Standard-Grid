#!/bin/sh
run_grid_instance (){
	python  ../../../../ml_root/ml_code.py  --bs 64 --lr_net 0.001 --epochs 5000 --STANDARDGRID_root 2525fdbb54fcdf20e68567f24652da350868ad5d148c542769a8c473cc7a74d1b83e64baa57f84be835e148f9a2879005cda6e34f88d6c2b83050dc26424ff4b --STANDARDGRID_hex 02e5e2a50e0ab62fc95734f97eec5c6b98e95f6580d217f741f460229273aa2a1deb0d403c6cc099e006216442c8a5016936373cdfaeec4708af992d99b3e52f 
 	echo "Exit code" $? > STANDARDGRID_instance_output
}
run_grid_instance