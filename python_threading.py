import threading
import time

def myfunction():
    print("start a thread")
    time.sleep(3)
    print("end a thread")

# setup container to be fill by myfunction() 5 times
threads = []

# loop to start threading and append into the container
for i in range(5):
    th = threading.Thread(target=myfunction)
    th.start()
    threads.append(th)

# loop into threads lists, to start join threads between those 5 times myfunction
for member in threads:
    th.join()



