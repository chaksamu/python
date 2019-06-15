from time import sleep
from threading import *

class Hello(Thread):
    def run(self):           #run is default method
        for i in range(5):
            print("Hello")
            sleep(1)

t1=Hello()
#t1.run()
t1.start()
sleep(0.5)
class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)
t2=Hi()
#t2.run()
t2.start()

t1.join()   #Join will tell to main thread wait till completion of t1 and t2 thread.
t2.join()
print("By1")