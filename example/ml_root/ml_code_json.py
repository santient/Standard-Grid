import os
import time
import pickle
import standard_grid
import json

def get_arguments():
	parser = standard_grid.ArgParser()
	parser.register_parameter("--bs",int,32,"The batch size.")
	parser.register_parameter("--lr_net",float,0.001,"The learning rate of the model.")
	parser.register_parameter("--epochs",int,2000,"The number of epochs.")
	#This is necessary
	parser.register_parameter('--STANDARDGRID_root', str,".",'The grid root')

	args=parser.compile_argparse()

	return args 


if __name__=="__main__":

	params=get_arguments()
	#The most complex ML model
	time.sleep(10)

	results_dir="results/"

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	results={"bestloss":.00123,"worst_loss":.0123}
	res_f=open(os.path.join(results_dir,"best.txt"),"w")
#	res_f.write("hi,1__STANDARD_GRID_SEP__bye,12")
	res_f.write(json.dumps(results))

	pickle.dump([0.001,0.00123,0.00321],open(os.path.join(results_dir,"epochs.pkl"),"wb"))
	
