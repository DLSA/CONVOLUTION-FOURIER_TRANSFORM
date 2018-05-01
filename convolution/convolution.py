#Convolution of X[n] with impulse function H[n] of a discrete time LTI system.
import random

bias=10000 

print "\n\nPLEASE ENTER THE INPUT FUNCTION\n"
print "'You have to only enter the range of n for which you want x[n] to be non zero(-10000 to +10000 separated by spaces'"
print "ex: \n-5  3"
print "Random inputs will be generated between -5 & 3\nenter range:"
begin1,end1=raw_input().split()
begin1=int(begin1)
end1=int(end1)
begin1+=bias
end1+=bias
inputf=[0]*20000

for i in xrange(begin1,end1+1,1):
	inputf[i]=random.randint(-5,5)

print "\n\nPLEASE ENTER THE IMPULSE FUNCTION\n"
print "'You have to only enter the range of n for which you want h[n] to be non zero(-10000 to +10000 separated by spaces'"
print "ex: \n-5  3"
print "Random inputs will be generated between -5 & 3\nenter range:"
begin2,end2=raw_input().split()
begin2=int(begin2)
end2=int(end2)
begin2+=bias
end2+=bias
impulsef=[0]*20000
for i in xrange(begin2,end2+1,1):
	impulsef[i]=random.randint(-4,4)
convolute=[0]*50000
sf=0
while(sf!=(end1-begin1)+1):
	for i in xrange(begin2,end2+1,1):
		convolute[i+sf]=convolute[i+sf]+(inputf[begin1+sf]*impulsef[i])
	sf+=1

print "\n\n\nINPUT FUNCTION GENERATED IS:"
for i in xrange(begin1,end1+1,1):
	print inputf[i],"\t",
print "\n"
for i in xrange(begin1,end1+1,1):
	print i-10000,"\t",
print "\n\n\nIMPULSE FUNCTION GENERATED IS:"
for i in xrange(begin2,end2+1,1):
	print impulsef[i],"\t",
print "\n"
for i in xrange(begin2,end2+1,1):
	print i-10000,"\t",
print "\n\n\nCONVOLUION FUNCTION IS:"

a=begin1+begin2-10000-1
b=end1+end2-10000+1
for i in xrange(a,b+1,1):
	print convolute[i],"\t",
print "\n"
for i in xrange(a,b+1,1):
	print i-10000,"\t",
print"\n\n"

#graph plotting code using matplotlib
# "THE code from here onwards is for plotting input & impulse signal and their convolution that's why it is commented.This part can only be used after installing matplotlib library in your system."
"""
import matplotlib.pyplot as plt
plt.xlim(-15,15)
plt.ylim(-15,15)
plt.plot([-15,15],[0,0])
plt.plot([0,0],[-15,15])
plt.xlabel('X axis')
plt.ylabel('Y axis')

a=[0]
b=[0]
a.remove(0)
b.remove(0)
for i in xrange(begin1,end1+1,1):
	b.append(inputf[i])
for i in xrange(begin1,end1+1,1):
	a.append(i-10000)
for i in xrange(len(a)):
	plt.plot([a[i],a[i]],[0,b[i]],color='black',linewidth=5)
plt.title("INPUT SIGNAL")
plt.show()


import matplotlib.pyplot as plt
plt.xlim(-15,15)
plt.ylim(-15,15)
plt.plot([-15,15],[0,0])
plt.plot([0,0],[-15,15])
plt.xlabel('X axis')
plt.ylabel('Y axis')

a=[0]
b=[0]
a.remove(0)
b.remove(0)
for i in xrange(begin2,end2+1,1):
	b.append(impulsef[i])
for i in xrange(begin2,end2+1,1):
	a.append(i-10000)
for i in xrange(len(a)):
	plt.plot([a[i],a[i]],[0,b[i]],color='black',linewidth=5)
plt.title("Impulse SIGNAL")
plt.show()





import matplotlib.pyplot as plt
plt.xlim(-15,15)
plt.ylim(-15,15)
plt.plot([-15,15],[0,0])
plt.plot([0,0],[-15,15])
plt.xlabel('X axis')
plt.ylabel('Y axis')

a=[0]
b=[0]
a.remove(0)
b.remove(0)

m=begin1+begin2-10000-1
n=end1+end2-10000+1

for i in xrange(m,n+1,1):
	b.append(convolute[i])
for i in xrange(m,n+1,1):
	a.append(i-10000)
for i in xrange(len(a)):
	plt.plot([a[i],a[i]],[0,b[i]],color='black',linewidth=5)
plt.title("CONVOLUTION SUM")
plt.show()
"""
