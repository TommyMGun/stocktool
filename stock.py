from termcolor import colored
import datetime as dt
import pandas as pd
import pandas_datareader as web
import sys


def stock():
	print('\nplease delete old stock csv before trying to make a new one \n')

	start = dt.datetime(2000,1,1)
	end = dt.datetime.now()

	df = web.DataReader(input('Input company stock abbreviation: '), 'yahoo', start, end)
	df.to_csv('stock.csv')

	print(df)
	menu_loop()


def pyramid(rows=8):
    for i in range(rows):
        print(' '*(rows-i-1) + '*'*(2*i+1))


print('\n')
pyramid(12)
print('\n')


def menu():
	print('press 1 to get stocks for a company\n')
	print('press 2 to graph data from a csv\n')
	print('press 3 to exit\n')
	global choice 
	choice = int(input())
	return choice


#def graphing():
	


def menu_loop():
	err = colored('\nthat choice is invalid please try again\n', 'red', attrs=['blink'])
	while True:
		menu()
		if choice == 1:
			stock()
		elif choice == 2:
			print('the graphing feature not yet implemented\n')
		elif choice == 3:
			sys.exit()
		else:
			print(colored('\nthat choice is invalid please try again\n', 'red', attrs=['blink']))

			
menu_loop()

