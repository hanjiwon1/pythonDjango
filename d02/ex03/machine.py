#!/usr/bin/env python3
# coding: utf-8

import random
from beverages import *

class CoffeeMachine:
	def __init__(self):
		self.use = 0

	class EmptyCup(HotBeverage):
		def __init__(self):
			self.name = "empty cup"
			self.price = 0.90
		
		def description(self):
			return "An empty cup?! Gimme my money back!"

	class BrokenMachineException(Exception):
		def __init__(self):
			super().__init__("This coffee machine has to be repaired.")

	def repair(self):
		self.use = 0
		print("\n**machine is repaired !**\n")

	def serve(self, drink: HotBeverage):
		if self.use > 9:
			raise CoffeeMachine.BrokenMachineException
		self.use += 1
		if random.randint(0, 6) == 0:
			return CoffeeMachine.EmptyCup()
		return drink()

def machine_test():
	machine = CoffeeMachine()
	for i in range(25):
		try:
			print(machine.serve(random.choice([HotBeverage, Coffee, Tea, Cappuccino, Chocolate])))
		except machine.BrokenMachineException as e:
			print(e)
			machine.repair()


if __name__ == '__main__':
	machine_test()