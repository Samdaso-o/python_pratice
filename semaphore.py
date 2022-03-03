import threading
import time

sema = threading.Semaphore(5)

def code_execute():
    sema.acquire()
    time.sleep(1)

    count = 0
    for _ in range(100000):
        count += 1

    print(count)
    sema.release()

def execute():
    thread = threading.Thread(target=code_execute)
    thread.start()


# 비교 함수 
# def execute():
#     time.sleep(1)

#     count = 0
#     for _ in range(100000):
#         count += 1

#     print(count)



if __name__ == "__main__":
    start_time = time.time()
    print(start_time)

    execute()

    print(time.time()-start_time)