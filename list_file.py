import os

cwd = os.getcwd()
print(cwd)
os.chdir(cwd+"/Data/yolo/")
temp = os.getcwd()
print(temp)

file = open("/Users/eneskaranfil/Desktop/train.txt","w")
for index in os.listdir(temp):
    file.write(temp+"/"+index+"\n")