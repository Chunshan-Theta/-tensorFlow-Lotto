import csv
ArrayAward = []
ArrayAnsFactor=[]
with open('source.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        StringArray= ''.join(row)
        ArrayNumber = StringArray.split(',')
        ArrayAward.append(ArrayNumber)
#print ArrayAward
for index in range(4):
    for i in range(6):    
        ArraySample=[]
        for j in range(10):
            for k in range(6):            
                ArraySample.append(int(ArrayAward[j+index][2+k]))
        #ArraySample.sort()
        #print ArrayAward[index+10][i+2],ArraySample
        #print index,"*"*50
        ArrayAnsFactor.append([int(ArrayAward[index+10][i+2]),ArraySample])
#print ArrayAnsFactor[1]
import json
JsonArray = json.dumps(ArrayAnsFactor)
print JsonArray
