import simple_grid 
import os 
import sys

if __name__=="__main__":

	grid_status_checker=simple_grid.Grid_Resume(sys.argv[1])
	grid_status_checker.generate_resume()
