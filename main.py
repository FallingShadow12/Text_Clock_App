import time
from playsound import playsound
import datetime


def home_page():
    print("Hello! This is your personal calculator")
    choose = input("Press 'a' for alarm, press 't' for timer and 's' for stopwatch: ")

    if choose == "t":
        timer()

    if choose == "s":
        stopwatch()

    if choose == "a":
        alarm()


def alarm():
    print("Hello user")
    set_time1 = int(input("Write the first number in the time here (e.g 18 = 6 o'clock): "))
    set_time2 = int(input("Write the second number: "))
    set_time3 = int(input("Write the third number: "))

    now = datetime.datetime.now()
    alarm_time = datetime.datetime.combine(now.date(), datetime.time(set_time1, set_time2, set_time3))
    time.sleep((alarm_time - now).total_seconds())

    playsound('2019-04-20_-_Quiet_Time_-_David_Fesliyan.mp3')


def timer():
    print("Hello user")
    user_input = int(input("Set the amount of time until you want the alarm to go off (seconds): "))
    print("Set the alarm sound you want to play")
    sound_input = input("Press 'b' for birds or 'c' for calming music: ")

    print("Your alarm has been set")
    time.sleep(user_input)
    if sound_input == "b":
        playsound('Birds-chirping-sound-effect.mp3')

    if sound_input == "c":
        playsound('2019-04-20_-_Quiet_Time_-_David_Fesliyan.mp3')


def stopwatch():
    count = 0
    print("Hello user, this is a stopwatch")
    print("It will automatically stop after 10,000 seconds")
    start = input("Press 's' to start: ")

    for i in range(1, 10001):
        print(i)
        time.sleep(1)


home_page()
