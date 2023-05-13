
# Voice Recorder

## Intro
This code is about recording audio from the computer's microphone for a specified number of seconds. First, it uses the sounddevice library to record the audio and saves it to a file. It also uses threading to allow the user to stop the recording early if they want. The stop function is called in a separate thread and waits for a specified number of seconds. The main thread waits for the stop thread to finish or for the user to indicate that they want to stop the recording early. Finally, the code checks if the stop thread is still running, and if it is, it cancels the thread. Overall, the code records audio for a specified number of seconds and allows the user to stop the recording early if they want.

## About Code
Here's an explanation of the code line by line, in language that a child could understand:

```
import sounddevice
from scipy.io.wavfile import write
import threading
import time
from pydub import AudioSegment
```

These are import statements that load some libraries that we'll use later in the code. 

```
def rec(sec, gg):
    gg.start()
    print("start")
    start = time.time()
    rece = sounddevice.rec((sec*44100), samplerate=44100, channels=2)

    a = gg.join()

    if a == None:
        write("demo.wav", 44100, rece)
        print("end")
        end = time.time()
        run_time_second = end - start
        au = AudioSegment.from_wav("F:/vrecv/demo.wav")
        seconds = int(run_time_second)*1000
        first_some_seconds = au[:seconds]
        first_some_seconds.export("demo.wav", format="wav")
        sounddevice.stop()
        print("recorded")
        return 1
```

This is a function called `rec`, which stands for "record." It takes two arguments, `sec` and `gg`. Inside the function, we call `gg.start()` to start another function running in the background, and then print "start" to the console. We use `sounddevice.rec` to record audio for `sec` seconds, and then use `write` to save the audio to a file called "demo.wav." Then, we print "end" to the console, calculate how long the recording lasted, and use the `AudioSegment` library to trim the recording to the correct length. Finally, we use `export` to save the trimmed recording back to "demo.wav," stop the sound device, print "recorded" to the console, and return `1` to signal that the recording is finished.

```
def time_left(t):
    flag = False
    
    def stop(t):
        nonlocal flag
        for i in range(t):
            time.sleep(1)
            if i == t-1:
                print("The record is ended its too long.")
                flag = None
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
```

#### This is another function called `time_left`. It takes one argument, `t`, which is the number of seconds that we'll record audio for. Inside the function, we create a variable called `flag` and set it to `False`. Then, we define a nested function called `stop`, which also takes `t` as an argument. Inside `stop`, we create a `for` loop that runs for `t` iterations. On each iteration, we wait for one second using `time.sleep(1)` and then check if we've reached the end of the recording time. If we have, we print a message to the console saying that the recording is too long, set `flag`.
##### 14. The `rec` function is defined with two parameters: `sec` and `gg`. `sec` represents the number of seconds for recording audio and `gg` is a threading object that controls the duration of the recording.

##### 15. The `gg.start()` method is called to start the thread.

##### 16. A message "start" is printed to indicate that recording has started.

##### 17. The `time.time()` function is called to get the start time of the recording.

##### 18. The `sounddevice.rec()` function is called to start recording audio. The first parameter is the number of frames to record (calculated by multiplying the number of seconds by the sample rate), and the samplerate and channels arguments are set to 44100 and 2, respectively.

##### 19. The `gg.join()` method is called to wait for the thread to finish. This is done so that the recording is stopped when the duration specified in the thread has been reached.

##### 20. If the thread is finished (i.e., the recording duration has reached its limit), the audio is written to a file named "demo.wav" using the `write()` method from the `scipy.io.wavfile` module.

##### 21. A message "end" is printed to indicate that recording has ended.

##### 22. The end time of the recording is calculated using `time.time()` and subtracting the start time from it.

##### 23. The audio is loaded from the "demo.wav" file using the `AudioSegment.from_wav()` method from the `pydub` module.

##### 24. The run time of the recording is converted to milliseconds and used to select the first portion of the audio using the slicing operation.

##### 25. The selected portion of the audio is saved to a new file named "demo.wav" using the `export()` method.

##### 26. The `sounddevice.stop()` method is called to stop the audio recording.

##### 27. A message "recorded" is printed to indicate that recording has been successfully completed.

##### 28. The `time_left` function is defined with one parameter `t`, which represents the duration of the recording.

##### 29. A boolean variable `flag` is set to False.

##### 30. The `stop` function is defined with one parameter `t`. This function runs as a separate thread and counts down the number of seconds left until the recording is ended.

##### 31. A `for` loop is used to iterate over a range of numbers from 0 to `t`. The loop pauses for one second using the `time.sleep()` function for each iteration.

##### 32. Inside the loop, the `if` statement checks if the current iteration is the last one. If it is, a message "The record is ended its too long." is printed and `flag` is set to `None`.

##### 33. The function then returns the number of seconds elapsed.

##### 34. A new thread `t3` is created using the `threading.Thread()` method. The `target` parameter is set to `stop` function, and the `args` parameter is set to `t`.

##### 35. The `t3.start()` method is called to start the `t3` thread.

##### 36. The `s` function is defined with one parameter `t`. This function runs as a separate thread and prompts the user to enter any key to preview the recording after `t` seconds.

##### 37. The `input()` function is used to get the user's input.

##### 38. The `flag` variable is set to `True` to indicate that the recording should be stopped.

##### 39. The function then returns the user's input.

##### 40. A new thread `t4` is created using the `threading.Thread()` method. The `target` parameter is set to `s` function, and the `args.

### About Creator
Hi there! My name is Arpit Jaiswal, and I'm a passionate Python programmer. I enjoy working with Python and JavaScript, but my main focus is on Python programming. I love creating software solutions that solve complex problems and making them simple and efficient. I believe in constantly learning and growing as a programmer, and I'm always excited to take on new challenges.

#### Future updates
##### Adding new features like -
                        1. Pasue system.
                        2. Error handling etc.
                        3. Also convert it into Gui.
