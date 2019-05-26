#!/usr/bin/env python
#coding=utf-8
import random
import sys

sysCode=sys.getfilesystemencoding()

arr1 = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
arr2 = []
arr3 = ['1','0','X','9','8','7','6','5','4','3','2']

Info = {'idcard':'NULL', 'bithday':'NULL', 'sex':'NULL'}

def getint(min,max,zero=0):
	num = str(random.randint(min,max)).zfill(zero)
	return(num)

def isYear(year):
	if(year%4 == 0) & (year%100 != 0):
		return(True)
	elif year%400 == 0:
		return(True)
	else:
		return(False)

def mkdate(year):
	month = getint(1,12,2)
	big = [1,3,5,7,8,10,12]
	small = [4,6,9,11]

	if month in big:
		day = getint(1,31,2)
	elif month in small:
		day = getint(1,30,2)
	elif isYear(year):
		day = getint(1,29,2)
	else:
		day = getint(1,28,2)

	date = month+day
	return(date)

def BoyOrGirl(sex):
	if int(sex)%2 == 0:
		return('女'.decode('utf-8').encode(sysCode))
	else:
		return('男'.decode('utf-8').encode(sysCode))

def getInfo():
	Info['idcard'] = first + check
	Info['bown'] = (str(year)+" 年 "+birthday[0:2] + " 月 " + birthday[2:4] + " 日").decode('utf-8').encode(sysCode)
	Info['sex'] = BoyOrGirl(sex)

def showInfo():
	getInfo()
	print(Info['idcard'])
	print(Info['sex'])
	print(Info['bown'])



place = '110105'	#你我皆是朝阳群众
year = random.randint(1949,2017)
birthday = mkdate(year)
num = str(random.randint(0,99)).zfill(2)
sex = str(random.randint(0,9))

first = place+str(year)+birthday+num+sex

for i in range(17):
	arr2.append(int(first[i])*arr1[i])

sum = sum(arr2)
y = sum%11
check = arr3[y]

showInfo()

