import threading
import time

def show_thread():
# get current thread object
    poem="glgjssyqyhfbqz"
    print('Thread name:%s.' % threading.current_thread().name)
    for i in poem:
        print(i)
    time.sleep(1)
    print('Thread %s end.' % threading.current_thread().name)
t = threading.Thread(target=show_thread, name='elder')
t.start()

print('I\'m %s.' % threading.current_thread().name)

print('While %s is reading poems, I can donate one second.' % t.name)

print('wait one second for %s ' % t.name)

t.join()
print('%s ends after %s ended.' % (threading.current_thread().name, t.name))