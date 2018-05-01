#computation of DFT of discrete signal
import cmath
import random
import math

print "\n\nFOR INPUT SIGNAL please enter the value of N"
print "random values are generated for signal x[n]"
N=int(raw_input())
x=[0]*N
print "Do you want real or integer signal\n\t enter 1 for real, 2 for integer";
ch=int(raw_input())
for i in xrange(N):
	if(ch==1):
		x[i]=random.uniform(-10.0,10.0)
	elif(ch==2):
		x[i]=int(random.uniform(-10,10))
		
zreal=[0]*N
zimag=[0]*N
w=(2*math.pi)/N
for i in xrange(N):
	for j in xrange(N):
		zreal[i]+=x[j]*math.cos(w*i*j)
		zimag[i]-=x[j]*math.sin(w*i*j)
	

print "\n\nx[n] generated is :"
for i in xrange(N):		
	print round(x[i],3),"\t",
print "\n\n"
print "DFT of x[n] i.e. X[n] is :"	
for i in xrange(N):		
	print "(",round(zreal[i],3),round(zimag[i],3),"+j",")\t",
print "\n\n\n"

