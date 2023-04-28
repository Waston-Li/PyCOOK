lock_file = 'test.txt'
import fcntl
import time


def lock(f):
    fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)


def un_lock(f):
    fcntl.flock(f, fcntl.LOCK_UN)


from multiprocessing import Process


def open_file():
    try:
        f = open(lock_file, 'w')
        lock(f) # 加锁
        print('加锁成功')
    except Exception as e:
        print("加锁失败:")
        print(e)
        return
    
    print(f.read())
    time.sleep(10)
    un_lock(f)
    print("解除锁")
    f.close()

Process(target=open_file).start()
# time.sleep(8)
# Process(target=open_file).start()
