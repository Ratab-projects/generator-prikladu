import random
# random.randint(a, b)

operations = "+-*/"

"""
unary_operators = [ ["sinus", "sin(", ")"], 
					["cosinus", "cos(", ")"], 
					["brackets", "(", ")"] ]
					
binary_operators =[ ["plus", "+"], 
					["minus", "-"], 
					["multiplay", "*"],
					["divide", "/"] ]
"""


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
	

def hardGener(settings):
	operation = []
	leafs = 1
	idx = 0
	# generate
	if settings.number_of_operants >= 2:
		operation.append(Operation)
	while leafs < settings.number_of_operants:
		operator = random.choice(operators)
		print("Index:", idx, "operace:", operator)
		operation[idx].operator = operator[0]
		print("Index:", idx, "operace:", operation[idx].operator)
		operation[idx].leaf = False
		leafs = leafs -1
		if operator[1] == 1:	# unary
			leafs = leafs +1
			operation.append(Operation)
			operation[idx].operands_index = len(operation)-1
		elif operator[1] == 2:	# binary
			leafs = leafs +2
			operation.append(Operation)
			operation[idx].operands_index = len(operation)-1
			operation.append(Operation)
			operation[idx].operands_index = len(operation)-1
		# aktualizace
		idx = idx +1
		
	for i in range(len(operation)):
		print("Index:", i, operation[i].operator)
			
	# set leafs
	while leafs > 0:
		operation[idx].operator = random.randint(settings.minimum, settings.maximum)
		operation[idx].leaf = False
		#aktualizace
		idx = idx +1
		leafs = leafs -1
	
	for operation_to_print in operation:
		print(operation_to_print.operator)
	
	# colaps
	
	return operation[0].operator


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
	if operation == "-":
		result = param1-param2
	if operation == "*":
		result = param1*param2
	if operation == "/":
		result = param1/param2
	
	return result


def easyEval(operation):		# TODO
	queue = operation.copy()
	i = 1
	while i < len(queue)-1:
		#print(" Index: ", i, "/", len(queue))
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
		#for operant in queue:
		#	print (operant,"", end='')
		#print("")
	
	i = 1
	while i < len(queue)-1:
		#print(" Index: ", i, "/", len(queue))
		param1 = queue[i-1]
		operation = queue[i]
		param2 = queue[i+1]
		del queue[i-1]
		del queue[i-1]
		del queue[i-1]
		queue.insert(i-1, Compute(param1, operation, param2) )
		#for operant in queue:
		#	print (operant,"", end='')
		#print("")
	
	return queue.pop()
	
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
	def Evaluate(self):
		self.result = easyEval(self.operation)
	
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
		print("Set input parameters")
		
		# number interval
		print("Number interval: ");
		self.minimum = int(input(" Set min: "))
		self.maximum = int(input(" Set max: "))
		
		# operace
		print("Operations (1: +/-/*/: | 2: all)");
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
		
	
settings = Settings()
settings.Set()
#settings.Print()

print(" ---Examples---")
for i in range(settings.number_of_examples):
	example = Example()
	example.Generate(settings)
	example.Print()
	example.Evaluate()
	settings.examples.append(example)
	
settings.Print_examples()



settings.Kill()

