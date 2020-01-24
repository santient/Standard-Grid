from itertools import product
from simple_grid import log
from collections import OrderedDict 
import hashlib
import os

#class to generate/run/process grid search
class Grid_Interpreter:
	
	def __init__(self,grid_root,interpreter_function):

		grid_root=os.path.abspath(grid_root)

		if os.path.isdir(grid_root) is False:
			log.error("Grid root does not exist. Exiting ...!",error=True)

		self.grid_root=grid_root
		self.grid_central_command_id=grid_root.split("/")[-1]
		self.grid_local_command_ids=[f for f in list(os.listdir(self.grid_root)) if os.path.isdir(os.path.join(self.grid_root,f))]
		self.interpreter_function=interpreter_function
		
	def interpret(self,report_file="grid_report.csv",):
		
		interpretations=[]		

		for grid_local_command_id in self.grid_local_command_ids:

			try:
				interpretation,interpretation_header=self.interpreter_function(self.grid_root,grid_local_command_id)
				if interpretation==None or interpretation_header==None or len(interpretation)==0 or len(interpretation_header)==None:
					raise ValueError("Interpretation is empty")

				interpretation=[grid_local_command_id]+interpretation
				interpretation_header=["local_id"]+interpretation_header

			except Exception as e:
				log.error("Failed to interpret grid local instance %s, <<message>> %s"%(grid_local_command_id,str(e)),error=False)
				continue



			if len(interpretation)!=len(interpretation_header):
				log.error("Interpretation and its header have different sizes - csv will fail. Exiting ...!")
			interpretations.append(interpretation)

		#TODO: Check if the report file exists

		with open(os.path.join(self.grid_root,report_file),"w") as report_handle:
			self.write_report_row(interpretation_header,report_handle)
			for interpretation in interpretations:
				self.write_report_row(interpretation,report_handle)

		log.success("Report generated in %s"%os.path.join(self.grid_root,report_file))

	def write_report_row(self,row_list,report_handle):
		row_string=""
		for item in row_list:
			row_string+=str(item)+","
		report_handle.write(row_string[:-1]+"\n")
