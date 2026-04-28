import random
import math

DEBUG = False

operations = "+-*/"

#				[name, number of operands, charakter(1/2 parts)]
operators =   [ ["sinus", 1, "sin(", ")"], 
				["cosinus", 1, "cos(", ")"], 
				["brackets", 1, "(", ")"],
				["plus", 2, "+"], 
				["minus", 2, "-"], 
				["multiplay", 2, "*"],
				["divide", 2, "/"] ]

class Operation:
	def __init__(self):
		self.operator = []
		self.operands_index = []
		self.leaf = True
		
	def Print(self):
		print("Operator:", self.operator, "branches:", self.operands_index, "	is leaf?", self.leaf)

def makeLeaf(operation, idx):
	# je to list
	#if operation[idx].leaf == True:
	#	return operation[idx].operator
	# je to vetveni
	if operation[idx].leaf == False:
		if len(operation[idx].operands_index) == 1:
			operation[idx].operator.insert(1, makeLeaf(operation, operation[idx].operands_index[0]))
		elif len(operation[idx].operands_index) == 2:
			operation[idx].operator.insert(0, makeLeaf(operation, operation[idx].operands_index[0]))
			operation[idx].operator.insert(2, makeLeaf(operation, operation[idx].operands_index[1]))
			#operation[idx].Insert_operator(2, makeLeaf(operation, operation[idx].operands_index[1]))
			#operation[idx].Insert_operator(0, makeLeaf(operation, operation[idx].operands_index[0]))
		
	return operation[idx].operator
	
def Colaps(operation):
	example = []
	example = makeLeaf(operation, 0)
	return example

def One_array(struct):
	tangled = True
	while tangled:
		i = 0
		tangled = False
		while i < len(struct):
			if isinstance(struct[i], list) and len(struct[i]) == 3:
				tangled = True
				for j in range(len(struct[i])):
					struct.insert(j+i+1, struct[i][j])
				del struct[i]
			# aktualizace
			i = i +1
			
	return struct
	
def hardGener(settings):
	operation = []
	leafs = 1
	idx = 0
	# generate
	if settings.number_of_operants >= 2:
		operation.append(Operation())
		#operation[0].Print()
	while leafs < settings.number_of_operants:
		operator = random.choice(operators)
		#operation[idx].operator.append(operator[0])
		
		#print("Index:", idx, ":", end='')
		#operation[idx].Print()
		leafs = leafs -1
		if operator[1] == 1:	# unary
			operation[idx].operator.append(operator[2])
			operation[idx].operator.append(operator[3])
			operation[idx].leaf = False
			leafs = leafs +1
			operation.append(Operation())
			operation[idx].operands_index.append(len(operation)-1)
		elif operator[1] == 2:	# binary
			operation[idx].operator.append(operator[2])
			operation[idx].leaf = False
			leafs = leafs +2
			operation.append(Operation())
			operation[idx].operands_index.append(len(operation)-1)
			operation.append(Operation())
			operation[idx].operands_index.append(len(operation)-1)
		
		# aktualizace
		idx = idx +1
		#operation[idx-1].Print()
			
	# set leafs
	while leafs > 0:
		operation[idx].operator = random.randint(settings.minimum, settings.maximum)
		#aktualizace
		idx = idx +1
		leafs = leafs -1
		
	# kontrolni tisk
	for i in range(len(operation)):
		print("Index:", i, ":", end='')
		operation[i].Print()
	
	# colaps
	if DEBUG:
		print(" ---Colpas--")
	example = []
	example = Colaps(operation)
	print(example)
	if DEBUG:
		print(" ---One array--")
	array = []
	array = One_array(example)
	print(array)
	#exit()	# TODO
	
	return array

def Solve(operation, index1, index2):
	# vnitrek
	if len(operation) > 3:
		if DEBUG:
			print("Idx1:", index1+1, "idx2:", index2-1)
		operation.insert(index1+1, easyEval(operation, index1+1, index2-1) )
	
	# vnejsek
	if operation[index1] == "sin(":
		operation[index1+1] = math.sin(operation[index1+1])
	elif operation[index1] == "cos(":
		operation[index1+1] = math.cos(operation[index1+1])
	
	# ostraneni zavorek
	del operation[index1]
	del operation[index1+1]
	

def hardEval(operation):
	if DEBUG:
		print(" ---Hard eval---")
	hard = ["sin(", "cos(", "("]
	i = 0
	while i < len(operation):
		if operation[i] == ')':
			idx1 = 0
			idx2 = i
			for j in range(idx2-1, idx1, -1):
				if DEBUG:
					print(j)
				if operation[j] in hard:
					idx1 = j
					if DEBUG:
						print("Hard operation:", operation[j], "on index:", j, ") on index:", i)
					break
			Solve(operation, idx1, idx2)
			#if DEBUG:
			print(operation)
			i = 0
		else:
			i = i +1
	if len(operation) > 1:
		return easyEval(operation, 0, len(operation)-1)
	
	if DEBUG:
		print("operation out")
		print(operation)
	return operation[0]

def easyGener(settings):
	operation = []
	operation.append( random.randint(settings.minimum, settings.maximum) )
	for i in range(1,settings.number_of_operants):
		operation.append( random.choice(operations) )
		operation.append( random.randint(settings.minimum, settings.maximum) )
		if operation[-2] == '/' and operation[-1] == 0:
			operation[i*2] = 1
	return operation

def Compute(param1, operation, param2):
	if operation == "+":
		result = param1+param2
	elif operation == "-":
		result = param1-param2
	elif operation == "*":
		result = param1*param2
	elif operation == "/":
		result = param1/param2
	else:
		print("ERROR: operation:", operation)
	
	return result


def easyEval(queue, index1, index2):		# TODO
	i = index1+1
	j = len(queue)-1-index2
	while i < len(queue)-1-j:
		if DEBUG:
			print(" Index: ", i, "/", len(queue)-1-j)
		if queue[i] == "*" or queue[i] == "/":
			param1 = queue[i-1]
			operation = queue[i]
			param2 = queue[i+1]
			del queue[i-1]
			del queue[i-1]
			del queue[i-1]
			queue.insert(i-1, Compute(param1, operation, param2) )
		else:
			i = i+2
		if DEBUG:
			for operant in queue:
				print (operant,"", end='')
			print("")
	
	i = index1+1
	while i < len(queue)-1-j:
		if DEBUG:
			print(" Index: ", i, "/", len(queue)-1-j)
		param1 = queue[i-1]
		operation = queue[i]
		param2 = queue[i+1]
		del queue[i-1]
		del queue[i-1]
		del queue[i-1]
		queue.insert(i-1, Compute(param1, operation, param2) )
		if DEBUG:
			for operant in queue:
				print (operant,"", end='')
			print("")
	
	result = queue[index1]
	del queue[index1]
	return result
	
class Example:
	def __init__(self):
		self.operation = []
		self.result = 0
		
	# vygeneruje sekvenci prikladu
	def Generate(self, settings):
		if settings.difficulty == 1:
			self.operation = easyGener(settings);
		elif settings.difficulty == 2:
			self.operation = hardGener(settings);
	
	# vypocita vygenerovany priklad
	def Evaluate(self, settings):
		if settings.difficulty == 1:
			self.result = easyEval(self.operation.copy(), 0, len(self.operation)-1)
		elif settings.difficulty == 2:
			self.result = hardEval(self.operation.copy());
	
	# vytiskne 
	def Print(self):
		#print(" ---Example---")
		for operant in self.operation:
			print (operant,"", end='')
		print("=", self.result);
	

class Settings:
	# inicializace
	def __init__(self):
		self.difficulty = 0
		self.number_of_operants = 0
		self.minimum = 0
		self.maximum = 100
		self.number_of_examples = 0
		self.examples = []
	
	# uvolni pamet na konci programu	
	def Kill(self):
		while len(self.examples) > 0:
			self.examples.pop()
		
	# nacte nove paramtery z terminalu	
	def Set(self):
		print(" ---Settings--")
		print("Set input parameters")
		
		# number interval
		print("Number interval: ");
		self.minimum = int(input(" Set min: "))
		self.maximum = int(input(" Set max: "))
		
		# operace
		print("Operations (1: +/-/*/: | 2: all+sin()+cos() )");
		self.difficulty = int(input(" Set operations: "))
		self.number_of_operants = int(input(" Set number of operants: "))
		
		# pocet prikladu
		self.number_of_examples = int(input("Number of examples: "))
		
	# vytiskne stavajici nastaveni
	def Print(self):
		print(" ---Settings---")
		print("Difficulty: ", self.difficulty);
		print("Number of operants: ", self.number_of_operants);
		print("Min: ", self.minimum);
		print("Max: ", self.maximum);
		print("Number of examples: ", self.number_of_examples);
		
	def Print_examples(self):
		for i in range(self.number_of_examples):
			self.examples[i].Print()
		


