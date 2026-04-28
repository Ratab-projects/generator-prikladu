# Generator příkladů

30.6.2020

Pro spuštění programu:
```bash
python3 main.py
```

Se vás aplikace doptá jakým způsobem chcete příklady generovat:
```bash
 ---Settings--
Set input parameters
Type name of this set: 
 Set name: test
Number interval: 
 Set min: 0
 Set max: 10
Operations (0: +/- | 1: +/-/*/: | 2: all+sin()+cos() )
 Set operations: 1
 Set number of operants: 3
Number of examples: 10
```

Následně se vypíší vygenerované příklady a jejich výsledky:
```bash
 ---Examples---
6 / 8 / 2 = 0
8 * 4 * 4 = 0
8 / 5 - 2 = 0
7 - 3 + 8 = 0
9 - 0 - 10 = 0
4 / 7 + 8 = 0
4 + 8 + 10 = 0
3 + 1 + 4 = 0
10 * 10 + 3 = 0
0 + 3 / 9 = 0
6 / 8 / 2 = 0.375
8 * 4 * 4 = 128
8 / 5 - 2 = -0.3999999999999999
7 - 3 + 8 = 12
9 - 0 - 10 = -1
4 / 7 + 8 = 8.571428571428571
4 + 8 + 10 = 22
3 + 1 + 4 = 8
10 * 10 + 3 = 103
0 + 3 / 9 = 0.3333333333333333
```

Program také automaticky vygeneruje soubory:
- `examples.txt` - obsahuje vygenerované příklady
- `results.txt` - obsahuje výsledky vygenerovaných příkladů
- `all.txt` - příklady a výsledky v jednom souboru