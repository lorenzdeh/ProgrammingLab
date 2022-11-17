# Apro il file
my_file = open('shampoo_sales.txt', 'r')
# Leggo il contenuto
my_file_contents = my_file.read()
# Stampo a schermo i primi 50 caratteri
if len(my_file_contents) > 50:
    print(my_file_contents[0:50] + '...')
else:
    print(my_file_contents)
# Chiudo il file
my_file.close()

#   ----------------------------- #
#Leggere una riga, ogni readline() ci manda alla prossima riga
#print(my_file.readline())
#print(my_file.readline())
#print() aggiunge sempre alla fine il comando di "nuova linea"

#Modo più Pythonico e meglio per la ram quando si usano file grandi
my_file = open('shampoo_sales.csv', 'r')
for line in my_file:
    print(line)
my_file.close()

#   ----------------------------- #
#Lettura CSV, split e inserimento in due liste

# Inizializzo una lista vuota per salvare i valori
values = []
# Apro e leggo il file, linea per linea
my_file = open('shampoo_sales.csv', 'r')
for line in my_file:
    # Faccio lo split di ogni riga sulla virgola
    elements = line.split(',')
    # Se NON sto processando l’intestazione...
    if elements[0] != 'Date':
        # Setto la data e il valore
        date = elements[0]
        value = elements[1]
        # Aggiungo alla lista dei valori questo valore
        values.append(value)
