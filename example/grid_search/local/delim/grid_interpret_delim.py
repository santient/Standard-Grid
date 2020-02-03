import standard_grid
import pickle
import os 
import sys

if __name__=="__main__":
	grid=pickle.load(open(sys.argv[1],"rb"))
#	grid.default_interpret("results/best.txt","interpretation.csv")
	grid.json_interpret("results/best.txt","interpretation.csv")

