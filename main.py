list_2d = [[3, 5, 2],
           [10, 2, 7],
           [4, 1, 9]]

for row in list_2d:
    max_element = row[0]
    for element in row:
        if element > max_element:
            max_element = element
    print(max_element)

