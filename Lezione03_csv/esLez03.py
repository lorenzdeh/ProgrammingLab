def sum_csv(file_name):
    values = []
    file = open(file_name, 'r')
    for line in file:
        elements = line.split(',')
        if elements[0] != 'Date':
            value = elements[1]
            #.strip('\n')
            if isfloat(value):
                #Funziona ma dovrebbe esserci un altro modo per controllare se una variabile è float/int, ma da google al momento non trovo nulla che funzioni (isinstance(value, (float, int)), type(value) == float, non funzionano)
                values.append(float(value))
    file.close()
    if not values:
        return None
    else:
        return sum(values)


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
