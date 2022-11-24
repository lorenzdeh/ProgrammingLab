class CSVFile():

    def __init__(self, name):
        self.name = name

    def get_data(self):
        val = []
        file = open(self.name, 'r')
        for item in file:
            elements = item.split(',')
            if elements[0] != 'Date':
                elements[1] = elements[1].strip('\n')
                val.append(elements)
        file.close()
        return val


#file = CSVFile('shampoo_sales.csv')
#print(file.get_data())
