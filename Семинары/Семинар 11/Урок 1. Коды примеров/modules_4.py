"""Модуль modules"""
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..'))
from .files import chardet
import subprocess
#import chardet

ARGS = ['ping', 'yandex.ru']
YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
for line in YA_PING.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))
