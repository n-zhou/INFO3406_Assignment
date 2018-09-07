first = True
split = []
for line in open('csv/LATEST_SQL_QUERY.csv'):
    if first:
        first = False
    else:
        line = line.rstrip().split(',')[1:]
        print(line)
