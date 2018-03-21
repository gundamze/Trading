#coding:utf-8


import threading
import time

"""
Refrence: http://www.cnblogs.com/tkqasn/p/5700281.html

python--threading多线程总结
threading用于提供线程相关的操作，线程是应用程序中工作的最小单元。
python当前版本的多线程库没有实现优先级、线程组，线程也不能被停止、暂停、恢复、中断。

threading模块提供的类：
　　Thread, Lock, Rlock, Condition, [Bounded]Semaphore, Event, Timer, local。

threading 模块提供的常用方法：
　　threading.currentThread(): 返回当前的线程变量。
　　threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
　　threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。

threading 模块提供的常量：
　　threading.TIMEOUT_MAX 设置threading全局超时时间。


tread type:
    1. main thread
    2. front desk thread
    3. back desk thread
"""

###################################### test 0 #####################################
"""
Thread类
Thread是线程类，有两种使用方法，直接传入要运行的方法或从Thread继承并覆盖run()：

"""
#方法一：将要执行的方法作为参数传给Thread的构造方法
def action(arg):
    time.sleep(1)
    print 'the arg is:%s\r' %arg

for i in xrange(4):
    t =threading.Thread(target=action,args=(i,))
    t.start()

print 'main thread end!'

#方法二：从Thread继承，并重写run()
class MyThread(threading.Thread):
    def __init__(self,arg):
        super(MyThread, self).__init__()#注意：一定要显式的调用父类的初始化函数。
        self.arg=arg
    def run(self):#定义每个线程要运行的函数
        time.sleep(1)
        print 'the arg is:%s\r' % self.arg

for i in xrange(4):
    t =MyThread(i)
    t.start()

print 'main thread end!'





###################################### test 1 #####################################
"""
构造方法：
Thread(group=None, target=None, name=None, args=(), kwargs={})

　　group: 线程组，目前还没有实现，库引用中提示必须是None；
　　target: 要执行的方法；
　　name: 线程名；
　　args/kwargs: 要传入方法的参数。

实例方法：
　　isAlive(): 返回线程是否在运行。正在运行指启动后、终止前。
　　get/setName(name): 获取/设置线程名。

　　start():  线程准备就绪，等待CPU调度
　　is/setDaemon(bool): 获取/设置是后台线程（默认前台线程（False））。（在start之前设置）

　　　　如果是后台线程，主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不论成功与否，主线程和后台线程均停止
       　　如果是前台线程，主线程执行过程中，前台线程也在进行，主线程执行完毕后，等待前台线程也执行完成后，程序停止
　　start(): 启动线程。
　　join([timeout]): 阻塞当前上下文环境的线程，直到调用此方法的线程终止或到达指定的timeout（可选参数）。

"""

def action(arg):
    time.sleep(1)
    print  'sub thread start!the thread name is:%s\r' % threading.currentThread().getName()
    print 'the arg is:%s\r' % arg
    time.sleep(1)


for i in xrange(4):
    t = threading.Thread(target=action, args=(i,)) # setup thread
    t.start() # start the thread

print 'main thread end!'

"""
验证了serDeamon(False)(默认)前台线程，主线程执行过程中，前台线程也在进行，
主线程执行完毕后，等待前台线程也执行完成后，主线程停止。
"""


import threading
import time

def action(arg):
    time.sleep(1)
    print  'sub thread start!the thread name is:%s\r' % threading.currentThread().getName()
    print 'the arg is:%s\r' %arg
    time.sleep(1)

for i in xrange(4):
    t =threading.Thread(target=action,args=(i,))
    t.setDaemon(True)#设置线程为后台线程
    t.start()

print 'main_thread end!'

"""
验证了serDeamon(True)后台线程，主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不论成功与否，主线程均停止。
主线程A启动了子线程B，调用b.setDaemaon(True)，则主线程结束时，会把子线程B也杀死，与C/C++中得默认效果是一样的。

"""


###################################### test 2 #####################################


thread_list = []    # the list of thread

for i in xrange(4):
    t = threading.Thread(target=action, args=(i,)) # setup thread
    thread_list.append(t) # put thread to a list

for t in thread_list:
    t.start() # start the thread

for t in thread_list:
    t.join() # halt untill all sub thread finished, then execute the following codes/main thread

print 'main thread end!'

"""
验证了 join()阻塞当前上下文环境的线程，直到调用此方法的线程终止或到达指定的timeout，
即使设置了setDeamon（True）主线程依然要等待子线程结束。
"""

###################################### test 3 #####################################

for i in xrange(4):
    t =threading.Thread(target=action,args=(i,))
    t.setDaemon(True)
    t.start()
    t.join()

print 'main_thread end!'

"""
join不妥当的用法，使多线程编程顺序执行.
可以看出此时，程序只能顺序执行，每个线程都被上一个线程的join阻塞，使得“多线程”失去了多线程意义。
"""

###################################### test 4 #####################################


"""
Lock、Rlock类


　　由于线程之间随机调度：某线程可能在执行n条后，CPU接着执行其他线程。为了多个线程同时操作一个内存中的资源时不产生混乱，我们使用锁。
Lock（指令锁）是可用的最低级的同步指令。Lock处于锁定状态时，不被特定的线程拥有。Lock包含两种状态——锁定和非锁定，以及两个基本的方法。

可以认为Lock有一个锁定池，当线程请求锁定时，将线程至于池中，直到获得锁定后出池。池中的线程处于状态图中的同步阻塞状态。

RLock（可重入锁）是一个可以被同一个线程请求多次的同步指令。RLock使用了“拥有的线程”和“递归等级”的概念，处于锁定状态时，

RLock被某个线程拥有。拥有RLock的线程可以再次调用acquire()，释放锁时需要调用release()相同次数。
可以认为RLock包含一个锁定池和一个初始值为0的计数器，每次成功调用 acquire()/release()，计数器将+1/-1，为0时锁处于未锁定状态。

简言之：Lock属于全局，Rlock属于线程。

构造方法：
Lock()，Rlock（）,推荐使用Rlock()

实例方法：
　　acquire([timeout]): 尝试获得锁定。使线程进入同步阻塞状态。
　　release(): 释放锁。使用前线程必须已获得锁定，否则将抛出异常。

"""


gl_num = 0

def show(arg):
    global gl_num
    time.sleep(1)
    gl_num +=1
    print '%s\n' %gl_num

for i in range(50):
    t = threading.Thread(target=show, args=(i,))
    t.start()

"""
多次运行可能产生混乱。这种场景就是适合使用锁的场景。
"""

###################################### test 5 #####################################


gl_num = 0

lock = threading.RLock()

def show():
    lock.acquire() # the global variable is locked
    global gl_num
    gl_num += 1
    time.sleep(1)
    print '%s\n' %gl_num
    lock.release() # untill release, other thread could visit global variable

for i in range(50):
    t = threading.Thread(target=show)
    t.start()

"""
可以看出，全局变量在在每次被调用时都要获得锁，才能操作，因此保证了共享数据的安全性
"""


###################################### test 6 #####################################


"""
Condition类
　　Condition（条件变量）通常与一个锁关联。需要在多个Contidion中共享一个锁时，可以传递一个Lock/RLock实例给构造方法，
    否则它将自己生成一个RLock实例。
　　可以认为，除了Lock带有的锁定池外，Condition还包含一个等待池，池中的线程处于等待阻塞状态，
    直到另一个线程调用notify()/notifyAll()通知；得到通知后线程进入锁定池等待锁定。

构造方法：
Condition([lock/rlock])

实例方法：
　　acquire([timeout])/release(): 调用关联的锁的相应方法。
　　wait([timeout]): 调用这个方法将使线程进入Condition的等待池等待通知，并释放锁。使用前线程必须已获得锁定，否则将抛出异常。
　　notify(): 调用这个方法将从等待池挑选一个线程并通知，收到通知的线程将自动调用acquire()尝试获得锁定（进入锁定池）；
            其他线程仍然在等待池中。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。
　　notifyAll(): 调用这个方法将通知等待池中所有的线程，这些线程都将进入锁定池尝试获得锁定。调用这个方法不会释放锁定。
            使用前线程必须已获得锁定，否则将抛出异常。
"""


import threading
import time
condition = threading.Condition()
products = 0

class Producer(threading.Thread):
    def run(self): # run is the method in "module threading", you can override this method
        global products
        while True:
            if condition.acquire():#尝试获取锁，如果获得返回true
                if products < 10:
                    products += 1
                    print "Producer(%s):deliver one, now products:%s" %(self.name, products)
                    condition.notify()#不释放锁定，因此需要下面一句
                    condition.release()
                else:
                    print "Producer(%s):already 10, stop deliver, now products:%s" %(self.name, products)
                    condition.wait() #自动释放锁定,进入等待池，等待条件变量notify
                time.sleep(2)


class Consumer(threading.Thread):
    def run(self):
        global products
        while True:
            if condition.acquire():
                if products > 1:
                    products -= 1
                    print "Consumer(%s):consume one, now products:%s" %(self.name, products)
                    condition.notify()
                    condition.release()
                else:
                    print "Consumer(%s):only 1, stop consume, products:%s" %(self.name, products)
                    condition.wait()
                time.sleep(2)


for p in range(0, 5):
    p = Producer()
    p.start()

for c in range(0, 2):
    c = Consumer()
    c.start()


###################################### test 6.1 #####################################
"""
notifyAll()
"""
import threading

alist = None
condition = threading.Condition()

def doSet():
    if condition.acquire():
        while alist is None:
            condition.wait()
        for i in range(len(alist))[::-1]:
            alist[i] = 1
        condition.release()

def doPrint():
    if condition.acquire():
        while alist is None:
            condition.wait()
        for i in alist:
            print i,
        print
        condition.release()


def doCreate():
    global alist
    if condition.acquire():
        if alist is None:
            alist = [0 for i in range(10)]
            condition.notifyAll()
        condition.release()


tset = threading.Thread(target=doSet, name='tset')
tprint = threading.Thread(target=doPrint, name='tprint')
tcreate = threading.Thread(target=doCreate, name='tcreate')
tset.start()
tprint.start()
tcreate.start()



###################################### test 7 #####################################


"""
Event类
　　Event（事件）是最简单的线程通信机制之一：一个线程通知事件，其他线程等待事件。Event内置了一个初始为False的标志，
    当调用set()时设为True，调用clear()时重置为 False。wait()将阻塞线程至等待阻塞状态。
　　Event其实就是一个简化版的 Condition。Event没有锁，无法使线程进入同步阻塞状态。

构造方法：
Event()

实例方法：
　　isSet(): 当内置标志为True时返回True。
　　set(): 将标志设为True，并通知所有处于等待阻塞状态的线程恢复运行状态。
　　clear(): 将标志设为False。
　　wait([timeout]): 如果标志为True将立即返回，否则阻塞线程至等待阻塞状态，等待其他线程调用set()。
"""


import threading
import time

event = threading.Event()

def func():
    # 等待事件，进入等待阻塞状态
    print '%s wait for event...' % threading.currentThread().getName()
    event.wait()

    # 收到事件后进入运行状态
    print '%s recv event.' % threading.currentThread().getName()


t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t1.start()
t2.start()

time.sleep(2)

# 发送事件通知
print 'MainThread set event.'
event.set()




###################################### test 8 #####################################


"""
timer类
　　Timer（定时器）是Thread的派生类，用于在指定时间后调用一个方法。

构造方法：
Timer(interval, function, args=[], kwargs={})
　　interval: 指定的时间
　　function: 要执行的方法
　　args/kwargs: 方法的参数

实例方法：
Timer从Thread派生，没有增加实例方法。
"""
import threading

def func():
    print 'hello timer!'

timer = threading.Timer(5, func)
timer.start()




###################################### test 9 #####################################


"""
local类
　　local是一个小写字母开头的类，用于管理 thread-local（线程局部的）数据。对于同一个local，
线程无法访问其他线程设置的属性；线程设置的属性不会被其他线程设置的同名属性替换。

　　可以把local看成是一个“线程-属性字典”的字典，local封装了从自身使用线程作为 key检索对应的属性字典、
再使用属性名作为key检索属性值的细节。
"""
import threading

local = threading.local()
local.tname = 'main'

def func():
    local.tname = 'notmain'
    print local.tname

t1 = threading.Thread(target=func)
t1.start()
t1.join()

print local.tname

