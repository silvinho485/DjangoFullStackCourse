#!/bin/python3
import cardapio
import calendar
from datetime import datetime
import time
import random
calendar.setfirstweekday(calendar.SUNDAY)

now = datetime.now()
year = str(now)[0:4]
month = str(now)[5:7]
day = str(now)[8:10]
clock = str(datetime.now()).split('-')[2].split()[1].split(':')
weekToday = calendar.weekday(int(year),
                             int(month),
                             int(day))

def format_timer(hour):
    return "{}:{} - {:.2f}s".format(hour[0], hour[1], float(hour[2]))

def weekday(day=weekToday):
    mydict = {0:cardapio.segunda,
              1:cardapio.terca,
              2:cardapio.quarta,
              3:cardapio.quinta,
              4:cardapio.sexta}
    return mydict[day]


# print(calendar.TextCalendar(firstweekday=6).formatyear(2018))

