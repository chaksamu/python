import os
import shutil
from os import path
import datetime
from datetime import date, time, timedelta
import time
from shutil import make_archive
import zipfile
from zipfile import ZipFile

def main():
    if(path.exists("chakri.txt")):
        src=path.realpath("chakri.txt");
        print(src)
    head, tail = path.split(src)
    print("path:" +head)
    print("path:" +tail)
    dst=src+".bak"
    shutil.copy(src, dst)
    shutil.copystat(src,dst)
    t=time.ctime(path.getmtime("chakri.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("chakri.txt")))
    print(datetime.datetime.fromtimestamp(path.getctime("chakri.txt")))
    print(datetime.datetime.fromtimestamp(path.getatime("chakri.txt")))
    #os.rename("chakri2.txt","chakri.txt")

    shutil.make_archive("chakri archive","zip",head)
with ZipFile("testchakri.zip","w") as newzip:
    newzip.write("chakri.txt")
    newzip.write("chakri.txt.bak")


main()