# Apro e leggo il file, linea per linea
file = open('shampoo_sales.csv', 'r') 

total_value = []

for line in file:
   # Faccio lo split di ogni riga sulla virgola
   elements = line.split(',')

   if elements[0] != 'date':

	date = elements[0]
	value = elements[1]
	total_value.append(float(value))

print(total_value)





