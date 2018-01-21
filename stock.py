import colorama
from termcolor import colored
import datetime as dt
import pandas as pd
import pandas_datareader as web
from matplotlib import pyplot as plt
from matplotlib import style
import sys

style.use('ggplot')
colorama.init()
##

print(colored('''\nMIT License

Copyright (c) 2017 Hesston Robertson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.\n''', 'yellow', attrs=['blink']))


def stock():
	print(colored('\nplease delete old stock csv before trying to make a new one \n', 'yellow', attrs=['blink']))

	start = dt.datetime(2000,1,1)
	end = dt.datetime.now()

	df = web.DataReader(input('Input company stock abbreviation: '), 'yahoo', start, end)
	df.to_csv('stock.csv')

	print(df)
	menu_loop()


def menu():
	print('press 1 to get stocks for a company\n')
	print('press 2 to graph data from a csv\n')
	print('press 3 to exit\n')
	global choice 
	choice = int(input())
	return choice


#def graphing():
	


def menu_loop():
	while True:
		menu()
		if choice == 1:
			stock()
		elif choice == 2:
			print(colored('the graphing feature not yet implemented\n', 'red', attrs=['blink']))
		elif choice == 3:
			sys.exit()
		else:
			print (colored('\nthat choice is invalid please try again\n', 'red', attrs=['blink']))

			
menu_loop()

