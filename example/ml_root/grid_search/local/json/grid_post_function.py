import standard_grid
import pickle
import os 
import sys

def recreate(inp,outp):
	with open(inp) as f:
		content=f.read()
		outp=open(outp,"w")
		outp.write(content)

if __name__=="__main__":
	grid=pickle.load(open(sys.argv[1],"rb"))

	grid.apply(recreate,"output/best.txt","output/best2.txt")

