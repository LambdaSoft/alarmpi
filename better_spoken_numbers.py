#!/usr/bin/python
from math import floor

num2words = {0: 'Cero ', 1: 'Uno ', 2: 'Dos ', 3: 'Tres ', 4: 'Cuatro ', 5: 'Cinco ',
             6: 'Seis ', 7: 'Siete ', 8: 'Ocho ', 9: 'Nueve ', 10: 'Diez ',
            11: 'Once ', 12: 'Doce ', 13: 'Trece ', 14: 'Catorce ',
            15: 'Quince ', 16: 'Dieciseis ', 17: 'Diecisiete ', 18: 'Dieciocho ',
            19: 'Diecinueve ', 20: 'Veinte ', 30: 'Treinta ', 40: 'Cuarenta ',
            50: 'Cincuenta ', 60: 'Sesenta ', 70: 'Setenta ', 80: 'Ochenta ',
            90: 'Noventa '}

date2words = {1: 'Uno', 2: 'Dos', 3: 'Tres', 4: 'Cuatro', 5: 'Cinco',
             6: 'Seis', 7: 'Siete', 8: 'Ocho', 9: 'Nueve', 10: 'Diez',
            11: 'Once', 12: 'Doce', 13: 'Trece', 14: 'Catorce',
            15: 'Quince', 16: 'Dieciseis', 17: 'Diecisiete', 18: 'Dieciocho',
            19: 'Diecinueve', 20: 'Veinte', 30: 'Treinta'}

def n2w(n):
  if n<=20:
    return num2words[n]
  elif n<100:
    words=num2words[n-n%10]
    if n%10>0:
      words+=num2words[n%10]
    return words
  elif n<1000:
    hundreds=(n-n%100)/100
    tens=(n%100)-(n%100)%10
    singles=n-((hundreds*100)+tens)
    words=num2words[hundreds] + ' ciento'
    if tens > 0:
      words+=' '+num2words[tens]
    if singles > 0:
      words+=num2words[singles]
    return words
  elif n<1000000:
    thousands=(n-n%1000)/1000
    remainder=n-(thousands*1000)
    words=n2w(thousands)+' mil'
    if remainder>0:
      words+=' '+n2w(remainder)
    return words
  elif n<1000000000:
    millions=(n-n%1000000)/1000000
    remainder=n-(millions*1000000)
    words=n2w(millions)+' millon'
    if remainder>0:
      words+=' '+n2w(remainder)
    return words
  else:
    return 'Numero fuera de rango'

def d2w(n):
  try:
    return date2words[n]
  except KeyError:
    try:
      return num2words[n-n%10] + date2words[n%10]
    except KeyError:
      return 'Fecha fuera de rango'


