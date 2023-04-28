import threading
import time
H = 0
H0 = 0
H1 = 0
H2 = 0
start_time = time.time()
Stop_threads = False

def hello0():            
    while True:
        global H0
        H0 += 1
        print("hell0_" + str(H0)+'\n')
        global Stop_threads
        if Stop_threads:
            Stop_threads = False
            break
        time.sleep(10)


def hello1():
    while True:
        global H1
        H1+=1
        print("hell1_" + str(H1)+'\n')
        time.sleep(10)

def hello2():
    for i in range(3):
        global H2
        H2+=1
        print("hell2_" + str(H2)+'\n')
        time.sleep(20)

thread_funcs = {
    "hello0_thread": hello0,
    "hello1_thread": hello1,
    "hello2_thread": hello2,
}

def hello():            
    while True: 
        global H
        H+=1
        print("Hi_" + str(H)+'\n')
        time.sleep(30)

def check_thread(thread_func, thread_name):
    thread = threading.Thread(target=thread_func, name=thread_name)
    thread.daemon = True
    thread.start()

    while True:
    # 检测进程是否还在运行
        if not thread.is_alive():
    # 重启该线程
            print("Thread " + thread_name + " has stopped. Restarting...")
            thread = threading.Thread(target=thread_func, name=thread_name)
            thread.daemon = True
            thread.start()
            print("Thread " + thread_name + " restarted.")
        time.sleep(10)          #每隔10秒检测一次


ht = threading.Thread(target=hello,name="hello_thread")
ht.daemon = True            
ht.start()

threading.Thread(target=check_thread, args=(hello0, "hello0_thread"), name="h0_checker").start()
threading.Thread(target=check_thread, args=(hello1, "hello1_thread"), name="h1_checker").start()
threading.Thread(target=check_thread, args=(hello2, "hello2_thread"), name="h2_checker").start()


time.sleep(30)
print("执行全局标识")
current_time = time.time()
if current_time  >= start_time + 30 :
    Stop_threads = True

ht.join()      
