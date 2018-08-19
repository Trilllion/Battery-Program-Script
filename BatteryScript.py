import os
import time
import psutil
import subprocess

#CLASS TO STORE DATA
class process:
    p = []                      #Program address returned from openProgram
    x = 0                       #Counter to know if program was opened    
    dirPath = os.getcwd()       #Path of folder where script is placed
    numLines = 0                #Number of programs in txt
    programList = []            #Program paths returned from readFile
    filePath = ''
    checkFrequency = 60

#Opens the program
def openProgram(list):
    try: 
        ob.p.append(subprocess.Popen(list))
    except FileNotFoundError:
        print('')
    except OSError:
        print('')
    

#Closes the program
def closeProgram(p):
    p.terminate()

#Reads program paths from txt
def readFile():
    File = open(r"C:/a/a/Programs.txt", "r")
    l = File.readlines()
    File.close
    ob.programList = l


#Creates a file if it doesn't exist in the same folder as script, if not, opens it
def createFile():
    #Try creating files
    try:
        File = open(ob.dirPath + "\\Programs.txt", "x")
        print("Creating new Programs list file in " + ob.dirPath)
        print("Please open the txt file, and add programs line by line")
        print("Then restart the python script")
        File.close()
    #Try opening file
    except Exception as e:
        filePath = ob.dirPath + '\\Programs.txt'
        ob.filePath = filePath
        print("File already exists at " + filePath)
        print("Opening programs file")
        file = open(filePath.strip(), 'r')
        return file

def getTimePeriod():
    file = open(ob.filePath.strip(), 'r')
    #print(ob.programList)
   
    try:
        timer = int(ob.programList[0])
        ob.checkFrequency = timer
        print("Using custom Value")
    except ValueError :
        print("Using Defaults")

#Class object
ob = process()

createFile()
readFile()
getTimePeriod()
programList = len(ob.programList)

#Infinite loop, runs once every 60 seconds
while True:
    if psutil.sensors_battery().power_plugged and ob.x == 0:
        for i in range(len(ob.programList)):
            openProgram(ob.programList[i].strip())
        ob.x = 1    
    elif psutil.sensors_battery().power_plugged == False and ob.x == 1: 
        for k in range(len(ob.programList)):
            try : 
                print (ob.p[k])
                closeProgram(ob.p[k])
            except Exception as e:
                print(str(e))
        ob.x = 0           
    time.sleep(ob.checkFrequency)

    