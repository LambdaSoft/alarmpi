#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import json
import decimal
import time

from apcontent import alarmpi_content

class weather_yahoo(alarmpi_content):
  def build(self):
    location = self.sconfig['location']

    if self.sconfig['metric'] == str(1):
        metric = '%20and%20u%3D\'c\''
    else:
        metric = ''

    try:
        weather_url = "https://" + \
                      self.sconfig["host"] + \
                      self.sconfig["path"] + \
                      location + \
                      metric + \
                      self.sconfig['pathtail']
        weather_api = urllib.urlopen(weather_url)
        response = weather_api.read()
        response_dictionary = json.loads(response)

        current = response_dictionary['query']['results']['channel']['item']['condition']['temp']
        current_low = response_dictionary['query']['results']['channel']['item']['forecast'][0]['low']
        current_high = response_dictionary['query']['results']['channel']['item']['forecast'][0]['high']
        conditions = response_dictionary['query']['results']['channel']['item']['condition']['text']
        forecast_conditions = response_dictionary['query']['results']['channel']['item']['forecast'][0]['text']
        wind = response_dictionary['query']['results']['channel']['wind']['speed']
        wind_chill = response_dictionary['query']['results']['channel']['wind']['chill']
        sunrise = response_dictionary['query']['results']['channel']['astronomy']['sunrise']
        sunset = response_dictionary['query']['results']['channel']['astronomy']['sunset']



        if wind != '':
          if self.debug:
            print response_dictionary ['query']['results']['channel']['wind']['speed']
          wind = round(float(wind),1)

    #    print current
    #    print current_low
    #    print current_high
    #    print conditions
    #    print wind


        if conditions != forecast_conditions:
          conditions = conditions + ' comenzando a ' + forecast_conditions 
        weather_yahoo = 'El tiempo para hoy es de ' + str(conditions) + ' actualmente ' + str(current) + ' grados con una mínima de ' + str(current_low) + ' y una máxima de ' + str(current_high) + '.  '

    # Wind uses the Beaufort scale
        if self.sconfig['metric'] == str(1) and self.sconfig['wind'] == str(1):
          if wind < 1:
              gust = 'En calma'
          if wind > 1:
              gust = 'Con un aire ligero'
          if wind > 5:
              gust = 'Con una ligera brisa'
          if wind > 12:
              gust = 'Con una suave brisa'
          if wind > 20:
              gust = 'Con una brisa moderada'
          if wind > 29:
              gust = 'Con una brisa fresca'
          if wind > 39:
              gust = 'Con una fuerte brisa'
          if wind > 50:
              gust = 'Con altos vientos a ' + wind + 'kilometros por hora'
          if wind > 62:
              gust = 'Con vientos fuertes a ' + wind + 'kilometros por hora'
          if wind > 75:
              gust = 'Con un fuerte viento a ' + wind + 'kilometros por hora'
          if wind > 89:
              gust = 'Con vientos tormentosos a ' + wind + 'kilometros por hora'
          if wind > 103:
              gust = 'Con vientos violentamente tormentosos a ' + wind + 'kilometros por hora'
          if wind > 118:
              gust = 'Con vientos huracanados a ' + wind + 'kilometros por hora'
          if wind == '':
              gust = ''
          weather_yahoo = weather_yahoo + str(gust) + '.  '

        if (self.sconfig['wind_chill'] == str(1) and
            wind > 5 and
            int(time.strftime("%m")) < 4 or
            wind > 5 and
            int(time.strftime("%m")) > 10):
          weather_yahoo = weather_yahoo + ' Y una sensación térmica de ' + str(wind_chill) + '.  '

    except Exception:
      weather_yahoo = 'Fallo al conectar con Yahoo Weather.  '

    if self.debug:
      print weather_yahoo

    self.content = weather_yahoo
