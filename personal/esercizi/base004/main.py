# indentazione errata non permette lo svolgimento del programma
# commento(#) a una riga soltanto
# dichiaro due variabili che non hanno bisogno di comandi
# vengono create nel momento in cui gli assegno la stringa
x = "McRognoni"
y = "Burger King"

# indentazione normale
print(1234567890)

"""
commento con tripla virgoletta per commento multiplo
indentazione di un costrutto 
la parte di codice all'interno di esso deve essere distanziata dall'inizio del comando del costrutto(1)
non ha importanza quanto, può andare a capo quante volte si vuole, l'importante è che non sia sulla stessa colonna del comando(2)
le righe di codice in uno stesso costrutto devono trovarsi tutte sulla stessa colonna(3)
"""
# 1
if x > y:	
	print(y + " fa schifo!")
	
# 2
if x == y:
															print(x + " fa schifo!")
															
if y != x:
	
	
	print(y + " fa schifo!")

# 3
if y != x:
	if y > x:
		print(x + " fa schifo!")
		print(y + " fa schifo!")
