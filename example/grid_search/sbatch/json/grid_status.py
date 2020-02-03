import standard_grid
import pickle
import os 
import sys

if __name__=="__main__":
	grid=pickle.load(open(sys.argv[1],"rb"))
	grid.get_status()
