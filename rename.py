import os
import sys

class RenameTheFiles:
    def change_names(directory):
        print os.getcwd()
        counter = 1
        baseDir = directory
        os.chdir(baseDir)
        for filenames in os.listdir(baseDir):   
                dst = "p_"+ str(counter) +".jpg"
                src = os.path.join(baseDir,filenames)
                destination = os.path.join(baseDir,dst)
                os.rename(src,destination)
                counter = counter + 1


    if __name__ == "__main__":
        baseDir = sys.argv[1]
        print baseDir
        change_names(baseDir)
        print("DONE")
        

