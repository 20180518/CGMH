import pickle
data=pickle.load(open('output.pkl'))
g=open('assert_data.txt','w')
for line in data:
    for i in range(len(line)):
        g.write(str(line[i]))
        if i==len(line)-1:
            g.write('\n')
        else:
            g.write(' ')
g.close()