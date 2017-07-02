import threading
count = 0
mutex = threading.Lock()
def foo():
    global count
    for i in range(100000):
        with mutex:
            count = count + 1

threads = []
for i in range(5):
    threads.append(threading.Thread(target=foo))
    threads[-1].start()

for t in threads:
    t.join()

print(count)