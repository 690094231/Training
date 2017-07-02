import queue
import threading
count=0
q = queue.Queue()
def foo():
    global count
    q.put(count)
    count+=1

for i in range(10):
    t = threading.Thread(target=foo)
    t.start()

for i in range(10):
    s = q.get()
    print(s)