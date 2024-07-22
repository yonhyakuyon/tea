import time
import winsound
import shelve
import pyglet
import os


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def save_time(user_time):
    with shelve.open("settings") as db:
        db["time"] = user_time


def save_sound(sound_path):
    with shelve.open("settings") as db:
        db["sound"] = sound_path


def load_time():
    with shelve.open("settings") as db:
        return db["time"]


def load_sound():
    with shelve.open("settings") as db:
        return db["sound"]


def set_up():
    user_time = int(input("Enter time in seconds: "))
    user_sound = input("Enter sound (y/n): ")
    if user_sound == "y":
        sound_path = input("Enter sound PATH: ")
        save_sound(sound_path)
    else:
        save_sound(0)
    save_time(user_time)
    print("Settings saved")
    start_message()


def start_message():
    print("Please choose what u need:")
    print("If u start program first time please set up settings")
    print("To set up settings print !s")
    print("To run timer print !t")
    user_mode = input()
    if user_mode == "!s":
        set_up()
    elif user_mode == "!t":
        timer()


def timer():
    user_time = load_time()
    while True:
        s = 0  # iterible for seconds
        min = 0  # iterible for minutes
        for i in range(user_time):
            time.sleep(1)
            s += 1
            cls()
            print("Timer: " + str(s) + " seconds")
            if (s % 60) == 0:
                min += 1
                cls()
                print("Timer: " + str(min) + " minutes " + str(s / 60) + " seconds")
        if load_sound() == 0:
            for i in range(6):
                winsound.Beep(666, 700)
                i += 1
        else:
            mus = pyglet.resource.media(load_sound())
            mus.play()
            pyglet.app.run()
        cls()
        print("Timer finished")
        break


start_message()
