from itertools import product
from simple_grid import log
from collections import OrderedDict 
import hashlib
import os
import pickle
import sys
import time
import math

#def commonprefix(main_path,second_path):
#	main_path=os.path.join(main_path,'')
#	second_path=os.path.join(second_path,'')
#
#	main_list=main_path.split(os.sep)[:-1]
#	second_list=second_path.split(os.sep)[:-1]
#	shared_list=[]
#	for i in range(min(len(main_list),len(second_list))):
#		if main_list[i]!=second_list[i]:
#			break
#		else:
#			shared_list.append(main_list[i])
#
#	shared_path=os.sep.join(shared_list)
#	main_path_depth=len(main_path[len(shared_path)+1:].split(os.sep))-1
#	rel_second_path=(".."+os.sep)*main_path_depth+second_path[len(shared_path)+1:]
#
#	print(shared_path,main_path_depth,rel_second_path)


def get_hash(in_str):

	hash_object = hashlib.sha512(in_str.encode("utf-8"))
	return str(hash_object.hexdigest())

class Grid:

	def __init__(self,entry_, grid_root_,resume_on_retry_=True,grid_operator_=product):
		self.entry=os.path.relpath(entry_,grid_root_)
		if os.path.isfile(self.entry) is False:
			log.error("Entry point does not exist. Exiting ...!",error=True)

		self.grid_root=os.path.relpath(grid_root_,os.sep.join(sys.argv[0].split(os.sep)[:-1]))
		if os.path.isdir(self.grid_root) is False:
			os.makedirs(self.grid_root) 

		self.resume_on_retry=resume_on_retry_
		self.grid_operator=grid_operator_

		self.grid_parameters=OrderedDict()
		self.grid_generated=False

	def register(self,key,value):
		if self.grid_generated==True:
			log.error("Grid already generated, cannot register any more hypers. Exiting ...!",error=True)
		if type(key)!=str:
			log.error("Key to be registered is not a string. Exiting ...!",error=True)
		if type(value)!=list:
			log.error("Value to be registered is not a list. Exiting ...!",error=True)
		
		self.grid_parameters[key]=value
		log.status("%s registered in grid."%key)

	def generate_grid(self):
		grid_list=[]
		try:
			for key in list(self.grid_parameters.keys()):
				grid_list.append(self.grid_parameters[key])
		except:
			log.error("Grid cannot be generated, check your parameters. Exiting ...!",error=True)

		self.grid=list(self.grid_operator(*grid_list))
		self.grid_generated=True


		def create_grid_hash__():
			total_commands_str=[]
			#TODO: This can be done better - just need the list itself and not combinations
			for i in range(len(self.grid)):
				grid_args=self.gen_args(i)
				final_command=grid_args
				total_commands_str.append(final_command)
				self.grid_hash=get_hash("".join(total_commands_str))

		create_grid_hash__()

		self.grid_dir=os.path.join(self.grid_root,self.grid_hash)
		if os.path.isdir(self.grid_dir) is True:
			log.error("Identical grid already exists. Exiting ...!",error=True)

		log.success("Grid successfully generated.")

	def shuffle_grid(self):
		if self.grid_generated==False:
			log.error("Grid was not generated, cannot shuffle. Exiting ...!",error=True)

		log.warning("Not implemented yet")
		pass

	def __getitem__(self,i):
		if self.grid_generated==False:
			log.error("Grid is not generated, please call .generate first. Exiting ...!",error=True)
		else:
			return self.grid_item(i) 

	def grid_item(self,i):
		if self.grid_generated==False:
			log.error("Grid is not generated, cannot get item. Exiting ...!",error=True)
		output={}
		for key,j in zip(list(self.grid_parameters.keys()),range(len(list(self.grid_parameters.keys())))):
			output[key]=self.grid[i][j]
		return output 

	def gen_args(self,i):
		args=""
		item=self[i]
		for key in list(item.keys()):
			args+=" --%s %s"%(str(key),str(item[key]))
		return args


	def generate_shell_instances(self,prefix="",postfix=""):
		os.makedirs(self.grid_dir)
		instances_dir=os.path.join(self.grid_dir,"instances/")

		entry_point_relative_to_instance=os.path.join("../../../",self.entry)

		def write_shell_instance_content__(fhandle,command,command_hex):
			fhandle.write ("#!/bin/sh\n")
			fhandle.write ("run_grid_instance (){\n")
			fhandle.write("\t"+command+" --STANDARDGRID_root %s --STANDARDGRID_hex %s \n "%(self.grid_hash,command_hex))
			fhandle.write("\t%s > %s\n"%("echo \"Exit code\" $?","STANDARDGRID_instance_output"))
			fhandle.write ("}\n")
			fhandle.write ("run_grid_instance")
	
		def write_instance_parameters__(fhandle,grid_instance):
			pickle.dump(grid_instance,fhandle)

		for i in range(len(self.grid)):
			grid_instance=self.gen_args(i)
			command=prefix+" "+entry_point_relative_to_instance+" "+grid_instance
			command_hex=get_hash(command)
			command_dir=os.path.join(instances_dir,command_hex)
			os.makedirs(command_dir)

			local_sh_name=os.path.join(command_dir,command_hex+".sh")
			write_shell_instance_content__(open(local_sh_name,"w"),command,command_hex)

			instance_pkl_fname=os.path.join(command_dir,command_hex+".pkl")
			write_instance_parameters__(open(instance_pkl_fname,"wb"),grid_instance)

		log.success("Shell instances created for grid in %s"%self.grid_dir)


	def create_runner(self,fraction=1.0,num_runners=1,runners_prefix=["sh"],parallel=1):

		if parallel>3:
			log.error("Parallel cannot be higher than 3.",error=True)
		if fraction>1 or fraction<0:
			log.error("Fraction not in range [0,1].",error=True)

		caller_dir=os.path.join(self.grid_dir,"callers/")
		command_hexes = [gi for gi in os.listdir(os.path.join(self.grid_dir,"instances/")) if os.path.isdir(os.path.join(self.grid_dir,"instances/",gi))]

		def write_instance_caller_content__(fhandle,callee_path,command_hex):
			fhandle.write ("#!/bin/sh\n")
			fhandle.write ("cd %s\n"%callee_path)
			fhandle.write ("sh %s.sh\n"%command_hex)
			fhandle.write ("cd - > /dev/null\n")

		if not os.path.exists(caller_dir):
			os.makedirs(caller_dir)

			for command_hex in command_hexes:
				caller_fname=os.path.join(caller_dir,command_hex+".sh")
				write_instance_caller_content__(open(caller_fname,"w"),os.path.join("../instances/",command_hex),command_hex)

		#If the central command directory does not exist, then recreate it
		central_command_dir=os.path.join(self.grid_dir,"central/")
		if not os.path.exists(central_command_dir):
			os.makedirs(central_command_dir)

		#TODO: Decide which attempt it is 
		attempt_dir=os.path.join(self.grid_dir,"central/","attempt_1/")
		if not os.path.exists(attempt_dir):
			os.makedirs(attempt_dir)

		#TODO: Decide which attempt it is 
		group_dir=os.path.join(self.grid_dir,"central/","attempt_1/","groups/")
		if not os.path.exists(group_dir):
			os.makedirs(group_dir)

		main_handle=open(os.path.join(attempt_dir,"main.sh"),"w")

		split_len=math.ceil((len(self.grid)*fraction)/num_runners)
		for i in range(num_runners):
			this_hexes=command_hexes[i*split_len:(i+1)*split_len]
			group_handle=open(os.path.join(group_dir,"group_%d.sh"%i),"w")
			for this_hex in this_hexes: 
				group_handle.write("sh ../instances/%s.sh\n"%this_hex)
			

			

#	def operationalize(self, central_command_prefix, central_command_postfix, local_command_prefix, local_command_postfix, runner_command_prefix, runner_command_postfix):
#
#		grid_central_command_handle=open(os.path.join(this_grid_dir,"grid_central_command.sh"),"w")
#
#		for command,grid_instance in zip(total_commands_str,self.grid):
#
#			command_hex=get_hash(command)
#			command_dir=os.path.join(this_grid_dir,command_hex)
#			os.makedirs(command_dir)
#			local_sh_name=os.path.join(command_dir,command_hex+".sh")
#			local_grid_name=os.path.join(command_dir,command_hex+".pkl")
#			self.write_local_sh_content(open(local_sh_name,"w"),command,command_dir,command_hex)
#			self.write_local_grid_content(open(local_grid_name,"wb"),grid_instance)
#			self.write_central_sh_content(grid_central_command_handle,local_sh_name,central_command_prefix)


#	def write_central_sh_content(self,grid_central_command_handle,central_command_entry,central_command_prefix):
#		grid_central_command_handle.write("%s %s"%(central_command_prefix,central_command_entry))
#		if self.central_command_parallel:
#			grid_central_command_handle.write(" &\n")
#		else:
#			grid_central_command_handle.write("\n")


