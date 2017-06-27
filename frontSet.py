import csv
ArrayAward = []
ArrayAns = []
ArrayFoctor=[]
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
	    ArraySample_resource=[]
            for k in range(6):    
		 ArraySample_resource.append(int(ArrayAward[j+index][2+k]))       
            ArraySample.append(ArraySample_resource)
        #ArraySample.sort()
        #print ArrayAward[index+10][i+2],ArraySample
        #print index,"*"*50
        #print int(ArrayAward[index+10][i+2]),ArraySample
	ArrayFoctor.append(ArraySample)
	ans=int(ArrayAward[index+10][i+2])-1
	ArrayAns_resource=[]
	for Ln in range(48):
	    if Ln!=ans:
	        ArrayAns_resource.append(0)
	    else:
		ArrayAns_resource.append(1)
	ArrayAns.append(ArrayAns_resource)	
print ArrayFoctor[0]
print ArrayAns[0]
