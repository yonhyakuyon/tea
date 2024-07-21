import time
import winsound

while True:
    s = 0  # iterible for seconds
    min = 0  # minutes
    user_time = int(input("Введите время заварки в секундах: "))
    for i in range(user_time):
        time.sleep(1)
        s += 1
        if s % 60 == 0:
            min += 1
    for i in range(6):
        winsound.Beep(666, 700)
        i += 1
    break
