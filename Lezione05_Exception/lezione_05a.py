class CSVFile():
    #Il try-except l'ho messo sia nell'__init_ che in get_data per allenamento, basterebbe solo in uno dei due
    def __init__(self, name):
        self.name = name
        try:
            file = open(self.name, 'r')
            file.readline()
        except FileNotFoundError as e:
            print('Errore, file non trovato (in __init__): "{}"'.format(e))
        except Exception as e:
            print('Errore generico (in __init__): "{}"'.format(e))

    def get_data(self):
        val = []
        try:
            file = open(self.name, 'r')
            for item in file:
                elements = item.split(',')
                if elements[0] != 'Date':
                    elements[1] = elements[1].strip('\n')
                    val.append(elements)
            file.close()
            return val
        except FileNotFoundError as e:
            print('Errore, file non trovato: "{}"'.format(e))
            return ''
        except Exception as e:
            print('Errore generico: "{}"'.format(e))
            return ''


#file = CSVFile('shampoo_sales____.csv')
#print(file.get_data())
