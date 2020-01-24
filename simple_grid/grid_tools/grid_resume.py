from itertools import product
from simple_grid import log
from collections import OrderedDict 
import hashlib
import os
import time
from simple_grid import Grid_Status

#class to generate/run/process grid search
class Grid_Resume:
	
	def __init__(self,grid_root,output_path=None,status_function=None,resume_function=None):

		grid_root=os.path.abspath(grid_root)

		if os.path.isdir(grid_root) is False:
			log.error("Grid root does not exist. Exiting ...!",error=True)

		self.grid_root=grid_root
		self.grid_central_command_id=grid_root.split("/")[-1]
		self.grid_local_command_ids=[f for f in list(os.listdir(self.grid_root)) if os.path.isdir(os.path.join(self.grid_root,f))]

		#the status function required for resuming
		if status_function == None:
			grid_status_checker=Grid_Status(self.grid_root)
			self.status_checker=grid_status_checker.status_checker
		else:
			self.status_checker=status_function

		#the resume function for resuming
		if resume_function == None:
			self.generate_resume=self.default_resume_function
		else:
			self.generate_resume=resume_function

		#output shell script for the resume
		if output_path==None:
			resume_counter=1
			while True:
				if os.path.isfile(os.path.join(self.grid_root,"grid_central_resume_%d.sh"%resume_counter)) is False:
					break
				resume_counter+=1
			self.output_path=os.path.join(self.grid_root,"grid_central_resume_%d.sh"%resume_counter)
			self.output=open(self.output_path,"w")
		else:
			self.output_path=output_path
			self.output=open(self.output_path,"w")
	


	def default_resume_function(self,hard_resume=False):
		"""Grid resume default resume function 
			
		The default function for resuming a grid search 	
	
		# Arguments
			self: The object for the Grid_Resume
			hard_resume: Boolean variable for resuming grid search for both the runs which failed and have not yet started. Default value is False
		# Returns
			No returns
			
		"""
		successes,failures,unknown=self.status_checker()
		grid_central_command=open(os.path.join(self.grid_root,"grid_central_command.sh")).read().split("\n")

		resume_queue=failures
		if hard_resume==True:
			resume_queue+=unknown		

		for entry in resume_queue:
			for line in grid_central_command:
				if entry in line:
					self.output.write(line+"\n")
		log.success("Grid resume shell script written in %s"%self.output_path)
