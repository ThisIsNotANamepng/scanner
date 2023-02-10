import os
def scan(file):
  os.system("clamscan "+file)
  print("Scanned " + file)

def quarantine(file):
  pre, ext = os.path.splitext(file)
  os.rename(file, "quarantine/"+pre + '.susp')
  former = (pre + '.susp')

def checkDB():
  import subprocess
  batcmd="clamscan -V"
  result = subprocess.check_output(batcmd, shell=True)
  print("Database version: "+str(result))#Not correct, but replit doesn't privide right response
  #If DB is updated proceed, otherwise update
  
def initScan():
  checkDB()
  path = input("Directory or file to scan: ")
  if (os.path.exists(path)==False):
    print("Entered directory does not exist. Try another one")
  if os.path.isdir(path):  
    for filename in os.scandir(path):
      if filename.is_file():
        scan(filename.path)
  elif os.path.isfile(path):  
    scan(path)
  else:
    print("Path type is not recognized as a directory or file, try a supported path type")
    exit()

def initQuarantine():
  quarantine('santhis.exe')
  #Destroy this function once a detection can be derived from a file, just quarantine() it from the scan() function
  
    

  
  
  