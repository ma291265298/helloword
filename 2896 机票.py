import threading
import time


class TicketDB:
    def __init__(self):
        self.cnt = 5

    def getCnt(self):
        return self.cnt

    def sell_ticket(self):
        print('第{0}张票已售出'.format(self.cnt))
        time.sleep(1)
        self.cnt -= 1


def body1():
    global db
    global lock
    while True:
        lock.acquire()
        cnt = db.getCnt()
        if cnt > 0:
            db.sell_ticket()
            lock.release()
            time.sleep(1)
        else:
            lock.release()
            break


def body2():
    global db
    global lock
    while True:
        lock.acquire()
        cnt = db.getCnt()
        if cnt > 0:
            db.sell_ticket()
            lock.release()
            time.sleep(1)
        else:
            lock.release()
            break


if __name__ == '__main__':
    db = TicketDB()
    lock = threading.Lock()
    t1 = threading.Thread(target=body1)
    t1.start()
    t2 = threading.Thread(target=body2)
    t2.start()
