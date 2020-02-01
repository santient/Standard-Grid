#!/bin/sh
run_grid_instance (){
	python  ../../../../ml_root/ml_code.py  --bs 64 --lr_net 0.0001 --epochs 5000 --STANDARDGRID_root 2525fdbb54fcdf20e68567f24652da350868ad5d148c542769a8c473cc7a74d1b83e64baa57f84be835e148f9a2879005cda6e34f88d6c2b83050dc26424ff4b --STANDARDGRID_hex 80c7758c8597bff36cb8dd068237a075b2b9ccfb7eeb596bb3fa80087a0c280f7b37cbc8b00fdcafb598bc81e82b31e712f358fecf852737c1016ffa282a73ac 
 	echo "Exit code" $? > STANDARDGRID_instance_output
}
run_grid_instance