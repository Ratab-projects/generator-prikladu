#By Pytel
"""
Tato aplikace byla vytvorena za ucelem generovani jednoduchych prikladu z matematiky.
Obtiznosti:
1 - +,-,*,/
2 - +,-,*,/,sin,cos,()
"""

import lib

	
settings = lib.Settings()
settings.Set()
#settings.Print()

print(" ---Examples---")
for i in range(settings.number_of_examples):
	example = lib.Example()
	example.Generate(settings)
	example.Print()
	example.Evaluate(settings)
	settings.examples.append(example)
	
settings.Print_examples()
settings.Save_all()
settings.Save_examples()
settings.Save_results()

settings.Kill()
