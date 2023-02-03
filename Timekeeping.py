import random

seconds_in_week = 604800
current_second = 0
day_list = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

def current_day(current_second):
    current_day = current_second % seconds_in_week // (24 * 60 * 60)
    return day_list[current_day]

def current_hour(current_second):
    current_hour = current_second % (24 * 60 * 60) // (60 * 60)
    return current_hour






