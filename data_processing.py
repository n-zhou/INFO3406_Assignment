import csv
import math

def avg(list):
    return sum(list)/max(len(list),1)

def std(list):
    total = 0.0
    average = avg(list)
    for value in list:
        total += (value-average)**2
    # return sample populaton standard deviation
    return math.sqrt(total/(len(list)-1))

csv_reader = csv.reader(open('csv/LATEST_SQL_QUERY.csv'))
valence = []
arousal = []
dominance = []
first = True
for line in csv_reader:
    if first:
        first = False
        print(line)
    else:
        # ignore the title

        valence.append(float(line[1]))
        arousal.append(float(line[2]))
        dominance.append(float(line[3]))

output_file = open('output.txt', 'w')
output_file.write('Valence | max: %f | min: %f | standard deviation: %f\n' % (max(valence), min(valence), std(valence)))
output_file.write('arousal | max: %f | min: %f | standard deviation: %f\n' % (max(arousal), min(arousal), std(arousal)))
output_file.write('dominance | max: %f | min: %f | standard deviation: %f\n' % (max(dominance), min(dominance), std(dominance)))
