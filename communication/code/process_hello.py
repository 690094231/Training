import multiprocessing
def hello():
    print('Hello, world!')

if __name__ == '__main__':
    p = multiprocessing.Process(target=hello,name='hehe')
    p.start()
    p.join()