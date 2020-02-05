# Standard-Grid
Standard-Grid @ Standard-SDK: standard protocol for reporting grid search results for students advised by me.

# Preliminaries

Assume you have a code written in a particular language and library. Assume you have a workstation or a slurm-based cluster. Assume your code is under a directory called ml_root. This directory has two properties 1) it has the main entry point of your code, 2) no write operations outside this directory is made by your code.
We will call the entry point of your code as ml_code.x. In reality there are no requirements for python, c++ or any other language. ml_code.x takes commands from argv using stanard --command style of system arguments. 

Example:
```
python ml_code.py --lr 0.001 --dataset woopsi --bounding_boxes yolo66666.666 --openface_file closed_neck.wtf
```

Let's assume the above file writes some outputs (like experimenal outputs) to a a directory called results inside ml_root. Results can never be outside the ml_root. ml_code.x will create the directory if not existing. 

The above are not unreasonable assumptions. For example, if the results dir does not exist then your code will crash even if not going through a grid search.

# Grid Search

Create a folder within the 
