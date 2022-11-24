#funziona il locale, ma non su autograding
#from CSVFile import CSVFile


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
        file.close()

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


class NumericalCSVFile(CSVFile):

    def get_data(self):
        var = super().get_data()
        var_float = []
        for item in var:
            #for i in range(len(item)):
            for i, s_item in enumerate(item):
                try:
                    if i > 0:
                        item[i] = float(s_item.strip('\n'))
                except ValueError as e:
                    print('Errore Value was not a float: {}'.format(e))
                except Exception as e:
                    print('Errore generico: "{}"'.format(e))
            var_float.append(item)

        print("File: ", var_float)
        return var_float


if (1):
    file = NumericalCSVFile('shampoo_sales.csv')
    print(file.get_data())
