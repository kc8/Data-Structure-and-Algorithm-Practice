import Queue

def hotPotato(namelist, num):
    queue = Queue.Queue()
    for name in namelist: 
        queue.enqueue(name)
    while queue.size() > 1:  #keep going until nothing is left
        for i in range(num):
           queue.enqueue(queue.dequeue())
        queue.dequeue()
    return queue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
