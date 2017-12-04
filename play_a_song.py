#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ConfigParser
import subprocess

Config=ConfigParser.ConfigParser()
try:
  Config.read('alarm.config')
except:
  raise Exception('Disculpe, Error al leer el archivo alarm.config .')

subprocess.call('find '+ Config.get('main','musicfldr') + ' -name \'*.mp3\' | sort --random-sort| mpg123 -@ - -l 1 -g 60', shell=True)
