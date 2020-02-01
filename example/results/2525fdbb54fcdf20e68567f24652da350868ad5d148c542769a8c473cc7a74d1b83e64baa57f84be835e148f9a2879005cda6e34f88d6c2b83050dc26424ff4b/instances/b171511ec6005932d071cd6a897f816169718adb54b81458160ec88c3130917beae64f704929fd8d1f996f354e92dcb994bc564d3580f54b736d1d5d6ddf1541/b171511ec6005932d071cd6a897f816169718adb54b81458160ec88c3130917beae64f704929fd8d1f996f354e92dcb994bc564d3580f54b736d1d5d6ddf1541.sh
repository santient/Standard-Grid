#!/bin/sh
run_grid_instance (){
	python  ../../../../ml_root/ml_code.py  --bs 32 --lr_net 0.001 --epochs 100000000000 --STANDARDGRID_root 2525fdbb54fcdf20e68567f24652da350868ad5d148c542769a8c473cc7a74d1b83e64baa57f84be835e148f9a2879005cda6e34f88d6c2b83050dc26424ff4b --STANDARDGRID_hex b171511ec6005932d071cd6a897f816169718adb54b81458160ec88c3130917beae64f704929fd8d1f996f354e92dcb994bc564d3580f54b736d1d5d6ddf1541 
 	echo "Exit code" $? > STANDARDGRID_instance_output
}
run_grid_instance