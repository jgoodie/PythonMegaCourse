#!/usr/local/bin/python3 

import datetime,glob2


# datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
filename = str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")) + ".txt"
fl = glob2.glob("file[1-9].txt")
# f1 = open('/Users/jgoodman/Documents/HCP Anywhere/workspaces/PythonMegaCourse/file1.txt', 'r')
# f2 = open('/Users/jgoodman/Documents/HCP Anywhere/workspaces/PythonMegaCourse/file2.txt', 'r')
# f3 = open('/Users/jgoodman/Documents/HCP Anywhere/workspaces/PythonMegaCourse/file3.txt', 'r')
# f4 = open('/Users/jgoodman/Documents/HCP Anywhere/workspaces/PythonMegaCourse/'+filename, 'w')
# 
# fc1=f1.readlines()
# fc2=f2.readlines()
# fc3=f3.readlines()
# 
# for x in fc1, fc2, fc3:
#     f4.write(x[0] + "\n")
#     #print(x)
# 
# f1.close()
# f2.close()
# f3.close()
# f4.close()
with open('/Users/jgoodman/Documents/HCP Anywhere/workspaces/PythonMegaCourse/' + filename, 'a+') as f4:
    for x in fl:
        tmp = open(x, 'r')
        f4.write(tmp.read() + "\n")
        
    
    
    