#!/bin/python
# -*- coding: utf-8 -*-
import time
import better_spoken_numbers as bsn

from apcontent import alarmpi_content

class greeting(alarmpi_content):
  def build(self):
    day_of_month=str(bsn.d2w(int(time.strftime("%d"))))

    now = time.strftime("%A %B ") + day_of_month + ',' + time.strftime(" %I %M %p")

    if int(time.strftime("%H")) < 12:
      period = 'os días'
    if int(time.strftime("%H")) >= 12:
      period = 'as tardes'
    if int(time.strftime("%H")) >= 20:
      period = 'as noches'

    # reads out good morning + my name
    gmt = 'Buen' + period + ', '

    # reads date and time 
    day = ' es ' + now + '.  '

    greeting = gmt + self.sconfig['name'] + day

    if self.debug:
      print greeting

    self.content = greeting
