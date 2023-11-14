import re

with open("data_B02b.csv", 'r') as data:
    rows = data.readlines()
    is_correct = True
    for row in rows:
        row_read = row.strip().split(';')
        print(row_read)
        inp1 = row_read[1]
        inp2 = row_read[2]
        if len(row_read) != 3:
            is_correct = False
        #+ - one or more occurences
        if not re.match("^-?\d+$", inp1):
            print("here")
            is_correct = False
        if not re.match("^-?\d+$", inp2):
            print("here2")
            is_correct = False
        
    if is_correct:
        print("File is correct")
    else:
        print("File is not correct")