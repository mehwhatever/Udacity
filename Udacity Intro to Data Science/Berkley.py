file = open('Berkley.csv','r')
data=file.read().split('\n')
file.close()
data=data[1:len(data)-1]
m={}
f={}
for i in xrange(0,len(data),2):
    a=data[i].split(',')
    b=data[i+1].split(',')
    if a[1]=='Male':
        m[a[2]]=(int(a[3]),int(b[3]))
    else:
        f[a[2]]=(int(a[3]),int(b[3]))
prob={}
for i in m:
    prob[i]=((float(m[i][0])/(m[i][0]+m[i][1]))*100,(float(f[i][0])/(f[i][0]+f[i][1]))*100)
mprob=0.0
fprob=0.0
for i in prob:
    mprob+=prob[i][0]
    fprob+=prob[i][1]
print 'Male',mprob/len(prob)
print 'Female',fprob/len(prob)
