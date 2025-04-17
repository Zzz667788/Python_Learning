import sys
import csv
import tabulate
'''
data = [
    ['Cheese','$25.50','$39.95'],
    ['1 item', '$27.50', '$41.95'],
    ['2 items', '$29.50', '$43.95'],
    ['3 items', '$31.50', '$45.95'],
    ['Special', '$33.50', '$47.95']
]
file_path = 'sicilian.csv'
fieldnames = ['Sicilian Pizza','Small','Large']
with open(file_path,'w') as file:
   writer = csv.writer(file)
   writer.writerow(fieldnames)
   for row in data:
       writer.writerow(row)
'''
if len(sys.argv) != 2:
    exit()
elif sys.argv[1][-4:] == '.csv':
    filepath = sys.argv[1]
    try:
        with open(filepath,'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            rows = list(reader)
            print(tabulate.tabulate(rows,headers=header,tablefmt = 'grid'))
    except:
        print("error")
        sys.exit()
else:
    print('FilePath Error')
    sys.exit()