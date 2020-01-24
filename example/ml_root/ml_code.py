import os
import time
import pickle
import simple_grid


def get_arguments():
	parser = simple_grid.ArgParser()
	parser.register_parameter("--bs",int,32,"The batch size.")
	parser.register_parameter("--lr_net",float,0.001,"The learning rate of the model.")
	parser.register_parameter("--epochs",int,2000,"The number of epochs.")
	#This is necessary
	parser.register_parameter('--CMUGRID_root', str,".",'The grid root')

	args=parser.compile_argparse()

	return args 


if __name__=="__main__":

	params=get_arguments()
	#The most complex ML model
	time.sleep(2)

	results_dir=os.path.join(params.CMUGRID_hex,"results/")

	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)

	res_f=open(os.path.join(results_dir,"best.txt"))
	res_f.write("Some good results")

	pickle.dump([0.001,0.00123,0.00321],os.path.join(results_dir,"epochs.pkl"))
	
