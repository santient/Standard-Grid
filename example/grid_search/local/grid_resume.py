import standard_grid
import pickle
import time
import sys
import os

if __name__=="__main__":

	grid=pickle.load(open(sys.argv[1],"rb"))
	grid.resume_as_before()

