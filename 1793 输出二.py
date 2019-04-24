import time
import threading


def thiread_body():
    t = threading.current_thread()
    for i in range(10):
        print('Hello, World')
        time.sleep(1)


if __name__ == '__main__':
    t1 = threading.Thread(target=thiread_body)
    t1.start()
