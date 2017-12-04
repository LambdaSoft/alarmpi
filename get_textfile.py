#!/bin/python
# -*- coding: utf-8 -*-

from apcontent import alarmpi_content

class textfile(alarmpi_content):

  def build(self):
    textfile = 'Archivo de texto activado pero no puede ser leido.'

    try:
      with open(self.sconfig['filepath'], 'r') as myfile:
        textfile=myfile.read().replace('\n', '  ')
    except IOError:
      pass

    if self.debug:
      print textfile

    self.content = textfile
