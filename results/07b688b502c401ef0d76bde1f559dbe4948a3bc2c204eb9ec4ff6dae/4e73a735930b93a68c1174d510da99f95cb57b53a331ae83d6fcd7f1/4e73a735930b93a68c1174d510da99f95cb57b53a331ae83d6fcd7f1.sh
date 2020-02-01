#!/bin/sh
run_grid_instance (){
	sh  --bs 32 --lr_net 0.0001 --epochs 5000 --CMUGRID_root ../../results/07b688b502c401ef0d76bde1f559dbe4948a3bc2c204eb9ec4ff6dae/4e73a735930b93a68c1174d510da99f95cb57b53a331ae83d6fcd7f1 --CMUGRID_hex 4e73a735930b93a68c1174d510da99f95cb57b53a331ae83d6fcd7f1 
 	echo "Exit code" $? > ../../results/07b688b502c401ef0d76bde1f559dbe4948a3bc2c204eb9ec4ff6dae/4e73a735930b93a68c1174d510da99f95cb57b53a331ae83d6fcd7f1/CMUGRID_instance_output
}
run_grid_instance