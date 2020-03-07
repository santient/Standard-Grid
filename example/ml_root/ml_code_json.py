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

	args=parser.compile_argparse()

	return args 


if __name__=="__main__":

	params=get_arguments()
	#The most complex ML model
	time.sleep(10)

	out_dir="output/"

	if not os.path.isdir(out_dir):
		os.makedirs(out_dir)

	results={"bestloss":.00123,"worst_loss":.0123}

	#this is important for the standard-grid, but not required.
	res_f=open(os.path.join(out_dir,"best.txt"),"w")
	res_f.write(json.dumps(results))

	#you can also write whatever you like to other places within the out_dir
	pickle.dump([0.001,0.00123,0.00321],open(os.path.join(out_dir,"weights.pkl"),"wb"))
	exit(0)
