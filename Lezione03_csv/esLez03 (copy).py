def sum_csv(file_name):
    values = []
    file = open(file_name, 'r')
    for line in file:
        elements = line.split(',')
        if elements[0] != 'Date':
            value = elements[1].strip('\n')
            if value.isnumeric():
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
