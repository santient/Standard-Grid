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
	#TODO: TRAIN A ML MODEL - POPULATE RESULTS
	time.sleep(2)
	results={"bestloss":.00123,"worst_loss":.0123}
	#ML MODEL DONE


	results_dir="results/"
	if not os.path.isdir(results_dir):
		os.makedirs(results_dir)
	res_f=open(os.path.join(results_dir,"best.txt"),"w")

	delim="__STANDARD_GRID_SEP__"
	output_str=""
	for key in results:
		output_str+=key+","+str(results[key])+delim
	res_f.write(output_str[:-len(delim)])

