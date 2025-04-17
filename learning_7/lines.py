import sys
name = sys.argv[1:]
count = 0
if len(name) == 0:
    sys.exit('Too few command-line arguments')
elif len(name) == 1:
    if name[0][-3:] == '.py':
        try:
            with open(name[0],'r') as file:
                for line in file:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    else:
                        count += 1
        except FileNotFoundError:
            sys.exit('File does not exist')
        else:
            print(count)
    else:
        sys.exit('Not a Python file')
else:
    sys.exit('Too many command-line arguments')