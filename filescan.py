#virus scan program
import glob, re
#scan for signatures just like Semantec or other anti virus software
def checkForSignatures():
    ''' A function to scan the files for virus signatures '''
    print("########## Checking for virus signatures ##########")
    #get all programs in the current directory
    programs = glob.glob("*.py")
    for p in programs:
        thisFileInfected = False
        file = open(p, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            if(re.search("^# Starting virus code", line)):
                #found a virus
                print("ALERT !!!!! Virus found in file" + p)
                thisFileInfected = True
        if(thisFileInfected == False):
            print(p + " appears to be clean")
    print("########## End Section ##########")