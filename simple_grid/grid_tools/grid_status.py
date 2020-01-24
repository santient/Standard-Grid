from itertools import product
from simple_grid import log
from collections import OrderedDict 
import hashlib
import os
import time

#class to generate/run/process grid search
class Grid_Status:
	
	def __init__(self,grid_root,status_function=None):

		grid_root=os.path.abspath(grid_root)

		if os.path.isdir(grid_root) is False:
			log.error("Grid root does not exist. Exiting ...!",error=True)

		self.grid_root=grid_root
		self.grid_central_command_id=grid_root.split("/")[-1]
		self.grid_local_command_ids=[f for f in list(os.listdir(self.grid_root)) if os.path.isdir(os.path.join(self.grid_root,f))]

		if status_function == None:
			self.status_checker=self.default_status_checker
		else:
			self.status_checker=status_function

	def default_status_checker(self):
		successes=[]
		failures=[]
		unknown=[]
		for grid_local_command_id in self.grid_local_command_ids:

				local_path=os.path.join(self.grid_root,grid_local_command_id,"CMUGRID_instance_output")
				try:
					with open(local_path) as script_exit_code_handle:
						status=int(script_exit_code_handle.read().split("\n")[0].split("Exit code ")[-1])
						if status==0:
							successes.append(grid_local_command_id)
						else:
							failures.append(grid_local_command_id)
				except:
					unknown.append(grid_local_command_id)

		if len(successes)==len(self.grid_local_command_ids):
			log.success("Grid %s is fully finished"%self.grid_central_command_id)
		else:
			total_finished=float(len(successes))/len(self.grid_local_command_ids)
			total_failed=float(len(failures))/len(self.grid_local_command_ids)
			total_unknown=float(len(unknown))/len(self.grid_local_command_ids)

			log.status("%.2f percent finished for grid %s"%(total_finished*100,self.grid_central_command_id))
			log.status("%.2f percent failed for grid %s"%(total_failed*100,self.grid_central_command_id))
			log.status("%.2f percent unknown for grid %s"%(total_unknown*100,self.grid_central_command_id))

		return successes, failures, unknown

	
	

