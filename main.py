import os
APP_FOLDER =  r'D:\Education\Systeme Operationel'
totalFiles = 0
totalDir = 0
size = 0

for path, dirs, files in os.walk(APP_FOLDER):
    for f in files:
        fp = os.path.join(path, f)
        size += os.path.getsize(fp)

for base, dirs, files in os.walk(APP_FOLDER):
    print('Searching in : ',base)
    for directories in dirs:
        totalDir += 1
    for Files in files:
        totalFiles += 1


print("Folder size: " + str(size))
print('Total number of files',totalFiles)
print('Total Number of directories',totalDir)