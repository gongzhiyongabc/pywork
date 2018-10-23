from time import ctime, sleep
import threading

#音乐播放器
def music(func, loop):
    for i in range(loop):
        print('I was listening to %s!%s'%(func, ctime()))
        sleep(2)

#视频播放器
def movie(func, loop):
    for i in range(loop):
        print('I was at the %s!%s'%(func, ctime()))
        sleep(5)
#创建线程组
threads = []
#创建线程组t1，并添加到线程数组
t1 = threading.Thread(target=music, args=('爱情买卖', 2))
threads.append(t1)
#创建线程组t2，并添加到线程数组
t2 = threading.Thread(target=movie, args=('阿凡达', 2))
threads.append(t2)


if __name__ == '__main__':
    #启动线程
    for t in threads:
        t.start()
    #守护进程
    for t in threads:
        t.join()
    print('all end: %s' %ctime())

