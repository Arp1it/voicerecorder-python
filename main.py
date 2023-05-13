import sounddevice
from scipy.io.wavfile import write
import threading
import time
from pydub import AudioSegment


def rec(sec, gg):
    gg.start()
    print("start")
    start = time.time()
    # for i in range(0, sec):
    rece = sounddevice.rec((sec*44100), samplerate=44100, channels=2)

    a = gg.join()

    if a == None:
        write("demo.wav", 44100, rece)
        print("end")
        end = time.time()
        run_time_second = end - start
        # print(int(second))

        # sounddevice.wait(1)

        au = AudioSegment.from_wav("F:/vrecv/demo.wav")
        seconds = int(run_time_second)*1000
        first_some_seconds = au[:seconds]
        first_some_seconds.export("demo.wav", format="wav")
        sounddevice.stop()
        print("recorded")
        # print(rece)
        return 1

def time_left(t):
    flag = False
    
    def stop(t):
        nonlocal flag
        for i in range(t):
            time.sleep(1)
            if i == t-1:
                # print(i)
                print("The record is ended its too long.")
                flag = True
                return i

    t3 = threading.Thread(target=stop, args=(t,))
    t3.start()

    def s(t):
        nonlocal flag
        c = input(f"after {t} seconds it will stop then you can enter to preview it. If you want to stop between time then just press Enter: ")
        flag = True
        return c

    t4 = threading.Thread(target=s, args=(t,))
    t4.start()

    while True:
        """ In the code, t3.join(0) and t4.join(0) is used to check the status of the thread t3 without blocking the main thread. The argument 0 passed to the join method sets a timeout value of zero seconds. This means that the join method will return immediately, whether or not the thread has completed its execution.

        If the thread t3 has completed its execution, t3.join(0) and t4.join(0) will return None. If it is still running, t3.join(0) and t4.join(0) will return without waiting for it to complete.

        In summary, t3.join(0) and t4.join(0) is a non-blocking way to check if the thread t3 has completed its execution, and the 0 argument sets a timeout value of zero seconds to return immediately."""

        t3.join(0)
        t4.join(0)
        if flag:
            return 1
        if not (t3.is_alive() or t4.is_alive()):
            break

    if t3.is_alive():
        t3.cancel()
    if t4.is_alive():
        t4.cancel()
    return 0

a = int(input("enter time to record: "))
t2 = threading.Thread(target=time_left, args=(a,))
t1 = threading.Thread(target=rec, args=(a, t2))

t1.start()


t1.join()