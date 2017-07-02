import threading
def hello():
    print('Hello, world!')

t = threading.Thread(target=hello) # create a thread
t.start() # start up the thread
# Then to do something else