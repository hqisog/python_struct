#-*- coding:utf-8 -*-
import threading
import time
import  os



def booth(tid):
    global i
    global lock
#每个次只允许一个线程访问
    while True:
        lock.acquire()
        if i!=0:
            i=i-1
            print "窗口：",tid,",剩余票数：",i

            time.sleep(1)
        else:
            print "thread_id",tid,"no more tickets"
            os._exit(0)
        lock.release()
        time.sleep(1)
i=100
lock=threading.Lock()
#生成十个线程
for k in range(10):
    new_thread = threading.Thread(target=booth,args=(k,))
    new_thread.start()