import os.path
from os import path

def main():
    #path.exists("chakri.txt")
    print("file exist: "+str(path.exists('chakri.txt')))
    print("FILE EXISTS: "+str(path.exists('syniv.txt')))
    print("directory exists:"+ str(path.exists('myDirectory')))
    print("directory exists:" + str(path.exists('test')))
    print("is it file: "+str(path.isfile('chakri.txt')))
    print("is it dir: "+str(path.isdir('test')))
    print("is it file: " + str(path.isfile('chak.txt')))
    print("is it dir: " + str(path.isdir('text')))

main()

import pathlib
file=pathlib.Path("chakri.txt")
if(file.exists()):
    print("File exist")
else:
    print("File not exist")
    
