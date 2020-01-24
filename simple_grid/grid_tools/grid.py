from itertools import product
from simple_grid import log
from collections import OrderedDict 
import hashlib
import os
import pickle

def get_hash(in_str):
	hash_object = hashlib.sha224(in_str.encode("utf-8"))
	return str(hash_object.hexdigest())

#class to generate/run/process grid search
class Grid:
	
	def __init__(self,central_command_parallel=True,grid_operator=product):
		self.grid_operator=grid_operator
		self.grid_parameters=OrderedDict()
		self.central_command_parallel=central_command_parallel
		self.generated=False
		

	def register(self,key,value):
		if self.generated==True:
			log.error("Grid already generated, cannot register any more hypers. Exiting ...!",error=True)
		if type(key)!=str:
			log.error("Key to be registered is not a string. Exiting ...!",error=True)
		if type(value)!=list:
			log.error("Value to be registered is not a list. Exiting ...!",error=True)
			
		self.grid_parameters[key]=value
		log.status("%s registered in grid."%key)
	
	def generate(self):
		grid_list=[]
		try:
			for key in list(self.grid_parameters.keys()):
				grid_list.append(self.grid_parameters[key])
		except:
			log.error("Grid cannot be generated, check your parameters. Exiting ...!",error=True)

		self.grid=list(self.grid_operator(*grid_list))
		self.generated=True
		log.success("Grid created.")

	def __getitem__(self,i):
		if self.generated==False:
			log.error("Grid is not generated, please call .generate first. Exiting ...!",error=True)
		else:
			return self.grid_item(i) 

	def grid_item(self,i):
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
	
	def operationalize(self, grid_root, local_command_prefix,central_command_prefix):

		grid_root=os.path.abspath(grid_root)
		
		if os.path.isdir(grid_root) is False:
			os.makedirs(grid_root) 

		total_commands_str=[]

		for i in range(len(self.grid)):
			grid_args=self.gen_args(i)
			final_command=local_command_prefix+" "+grid_args
			total_commands_str.append(final_command)
			

		this_grid_dir=os.path.join(grid_root,get_hash("".join(total_commands_str)))

		if os.path.isdir(this_grid_dir) is True:
			log.error("Identical grid already exists. Exiting ...!",error=True)

		os.makedirs(this_grid_dir)

		grid_central_command_handle=open(os.path.join(this_grid_dir,"grid_central_command.sh"),"w")

		for command,grid_instance in zip(total_commands_str,self.grid):

			command_hex=get_hash(command)
			command_dir=os.path.join(this_grid_dir,command_hex)
			os.makedirs(command_dir)
			local_sh_name=os.path.join(command_dir,command_hex+".sh")
			local_grid_name=os.path.join(command_dir,command_hex+".pkl")
			self.write_local_sh_content(open(local_sh_name,"w"),command,command_dir,command_hex)
			self.write_local_grid_content(open(local_grid_name,"wb"),grid_instance)
			self.write_central_sh_content(grid_central_command_handle,local_sh_name,central_command_prefix)

		log.success("Grid operationalized in %s"%this_grid_dir)
		
	def write_central_sh_content(self,grid_central_command_handle,central_command_entry,central_command_prefix):
		grid_central_command_handle.write("%s %s"%(central_command_prefix,central_command_entry))
		if self.central_command_parallel:
			grid_central_command_handle.write(" &\n")
		else:
			grid_central_command_handle.write("\n")
			
	def write_local_grid_content(self,fhandle,grid_instance):
		pickle.dump(grid_instance,fhandle)

	def write_local_sh_content(self,fhandle,command,command_dir,command_hex):
		fhandle.write ("#!/bin/sh\n")
		fhandle.write ("run_grid_instance (){\n")
		fhandle.write("\t"+command+" --CMUGRID_root %s --CMUGRID_hex %s \n "%(command_dir,command_hex))
		fhandle.write("\t%s > %s\n"%("echo \"Exit code\" $?",os.path.join(command_dir,"CMUGRID_instance_output")))
		fhandle.write ("}\n")
		fhandle.write ("run_grid_instance")

if __name__=="__main__":
	grid=Grid()
	grid.register("lr",[1,2,3])
	grid.register("bs",[6,7,8])
	grid.generate()
	grid.dump_sh("/media/bighdd8/Amir/cache/")
