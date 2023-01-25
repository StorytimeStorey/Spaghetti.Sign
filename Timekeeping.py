# Timekeeping system, a system for keeping time.
# Created by Story
import random


seconds_in_week = 604800
current_second = 0
day_list = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

# current_day function takes the current_second variable and calculates which "day" it is on.
# it will then return that value to be used in The Gear.
def current_day(current_second):
    current_day = current_second % seconds_in_week // (24 * 60 * 60)
    return day_list[current_day]

# current_hour function takes the current_second variable and calculates which "hour" of the day it is on.
# it will then return that value to be used in The Gear.
def current_hour(current_second):
    current_hour = current_second % (24 * 60 * 60) // (60 * 60)
    return current_hour




