import csv
import sys

name_st = []
if len(sys.argv)==3:
    if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        file_name1 = sys.argv[1]
        file_name2 = sys.argv[2]
        try:
            with open(file_name1,'r') as file:
                reader = csv.reader(file)
                header = next(reader)
                rows = list(reader)
        except:
            sys.exit('Could not read invalid_file.csv')
        else:
                #print(type(rows),rows)
            for row in rows:
                first_name,last_name = row[0].split(',',1)
                house = row[1]
                name_st.append({'first':first_name,'last':last_name,'house':house})
            #print(name_st)
            with open(file_name2,'w') as file2:
                fieldnames = ['first','last','house']
                writer = csv.DictWriter(file2,fieldnames=fieldnames)
                writer.writerows(name_st)
    else:
        sys.exit('False filename')
elif len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
else:
    sys.exit('Too many command-line arguments')
