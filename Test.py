fname = input("Enter file name: ")
if len(fname) < 1: fname = "log.txt"
fh = open(fname)
count = 0

for line in fh:
    if 'select' in line and 'from' in line:
        # Get String after substring occurrence using partition() method
        line = line.partition('select')[2]
        print("select " + line)
    elif 'SELECT' in line and 'FROM' in line:
        line = line.partition('SELECT')[2]
        print("select " + line)
    elif 'where' in line and '= ?' in line:
        print(line)
    else:
        continue
