import os

PROJECTNAME = input("input_project_name:")

INPUTPATH = input(r"input_your_path:")

a = '\\'

list = ['obj', 'ref', '3dsmax', 'maya',]

path = INPUTPATH+a+PROJECTNAME

os.mkdir(path)

for list in list:
    
    os.mkdir (path+a+list)

