#!/bin/sh
run_grid_instance (){
	python  ../../../../ml_root/ml_code.py  --bs 64 --lr_net 0.001 --epochs 100000000000 --STANDARDGRID_root 2525fdbb54fcdf20e68567f24652da350868ad5d148c542769a8c473cc7a74d1b83e64baa57f84be835e148f9a2879005cda6e34f88d6c2b83050dc26424ff4b --STANDARDGRID_hex 84c6069fc06cd9eba0a2a8de399022bf414fa3e53896ba3828b110e11cc781adb1827e0cc2af92f8fba5b7647fe7d74455cd2bfbb307bfcc93f8819d48360bb0 
 	echo "Exit code" $? > STANDARDGRID_instance_output
}
run_grid_instance