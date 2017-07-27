#!/usr/bin/env python
# -*- coding: utf-8 -*-

class joueur():
	def __init__():
		self.tapis = 15
		self.bourse = 30
		
class plateau():
	def __init__(self):
		self.sol = [[0] * 9 for i in range(9)]

	def ecrire(self):
		for i in self.sol:
			k = ""
			for j in i:
				k += str(j) * 3 + "  "
			print(k)
			print(k)
			print()

def main():
	a = plateau()
	a.ecrire()
	
	return 0

if __name__ == '__main__':
	main()

