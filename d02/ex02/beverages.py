# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    beverages.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jiwhan <jiwhan@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/30 17:10:40 by jiwhan            #+#    #+#              #
#    Updated: 2021/07/30 19:00:26 by jiwhan           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3
# coding: utf-8

class HotBeverage:
	def __init__(self, price = 0.30, name = "hot beverage"):
		self.price = price
		self.name = name

	def description(self):
		return "Just some hot water in a cup."

	def __str__(self):
		return f"name : {self.name}\nprice : {self.price:.2f}\ndescription : {self.description()}"

class Coffee(HotBeverage):
	def __init__(self):
		self.name = "coffee"
		self.price = 0.40
	
	def description(self):
		return "A coffee, to stay awake."

class Tea(HotBeverage):
	def __init__(self):
		self.name = "tea"
		self.price = 0.30

	def description(self):
		return "Just some hot water in a cup."

class Chocolate(HotBeverage):
	def __init__(self):
		self.name = "chocolate"
		self.price = 0.50

	def description(self):
		return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
	def __init__(self):
		self.name = "cappuccino"
		self.price = 0.45

	def description(self):
		return "Un po’ di Italia nella sua tazza!"

def beverages():
	hb = HotBeverage()
	print(hb)
	co = Coffee()
	print(co)
	te = Tea()
	print(te)
	ch = Chocolate()
	print(ch)
	ca = Cappuccino()
	print(ca)
	
if __name__ == '__main__':
	beverages()