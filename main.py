import time
import winsound
import os

while True:
    s = 0  # iterible for seconds
    min = 0  # minutes
    user_time = int(input("Введите время заварки: "))
    for i in range(user_time):
        time.sleep(1)
        s += 1
        if s % 60 == 0:
            min += 1
    winsound.Beep(666, 1000)
