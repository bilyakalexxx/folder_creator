import os

PROJECTNAME = input("input_project_name:")

print ("path example :D:\\")

INPUTPATH = input(r"input_your_path:")

a = '\\'

b = 'Substance'

list = ['Ref', 'External','Substance', 'Marmoset', 'AE', 'Premiere', 'Renders', ]

list2 = ['tex', 'outer']

path = INPUTPATH+a+PROJECTNAME

os.mkdir(path)

for list in list:
    
    os.makedirs (path + a + list)

if list in list:
    os.makedirs (path + a + b + a + list2[0] )
    os.makedirs (path + a + b + a + list2[1] )

    










#if True:
#    print ("Done")