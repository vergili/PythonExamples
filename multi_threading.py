import sys
from Queue import Queue, Empty
from threading import Thread, current_thread
from pyquery import PyQuery
import os 


visited = set()
queue = Queue()
                    

def get_parser():

    def parse():
        i = 0
        while True:
            i= i+1

            print str(current_thread()) +  "...  i= " + str(i) + "\n" 

    return parse



if __name__ == '__main__':
    parser = get_parser()
    workers = []
    for i in range(5):
        worker = Thread(target=parser)
        worker.start()
        workers.append(worker)
    for worker in workers:
        worker.join()

