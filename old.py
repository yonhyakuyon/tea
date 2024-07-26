import time
import winsound
import shelve
import pyautogui
import os
from tkinter import *
from tkinter import ttk

main = Tk()
main.minsize(250, 5)
frm = ttk.Frame(main, padding=10)
frm.grid()
ttk.Label(frm, text="Tea Timer!").grid(column=0, row=0)


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def save_time(user_time):
    with open("settings.txt", "w") as db:
        db.write(str(user_time))


def save_sound(sound_path):
    with shelve.open("settings") as db:
        db["sound"] = sound_path


def load_time():
    with open("settings.txt", "r") as db:
        return db.read()


def load_sound():
    with shelve.open("settings") as db:
        return db["sound"]


def set_up():
    # main.destroy()
    get = pyautogui.prompt("Set up settings", "Set up settings", ["ok"])
    # user_sound = input("Enter sound (y/n): ")
    # if user_sound == "y":
    #     print("I hope u move your .mp3 file to same folder as this program")
    #     sound_path = input("Enter sound name: ")
    #     save_sound(sound_path)
    # else:
    #     save_sound(0)
    save_time(get)
    print("Settings saved")
    timer()


def start_message():
    TGREEN = "\033[32m"  # Green Text
    print(TGREEN + "Here will be timer :)")
    # print("If u start program first time please set up settings")
    # print("To set up settings print !s")
    # print("To run timer print !t")
    # user_mode = input()
    # if user_mode == "!s":
    #     set_up()
    #     cls()
    # elif user_mode == "!t":
    #     timer()
    #     cls()


def timer():
    main.destroy()
    user_time = int(load_time())
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
        for i in range(5):
            winsound.Beep(666, 700)
            i += 1
        cls()
        print("Timer finished")
        pyautogui.confirm("Timer finished", "Timer finished", ["ok"])
        break


ttk.Button(frm, text="Start timer", command=timer).grid(column=0, row=2)
ttk.Button(frm, text="Set up settings", command=set_up).grid(column=1, row=2)

start_message()
