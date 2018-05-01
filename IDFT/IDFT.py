# computation of IDFT of complex discrete signal
import cmath
import random
import math

print "\n\nFOR INPUT SIGNAL please enter the value of N"
print "random values are generated for signal x[n]"
N=int(raw_input())
Xreal=[0]*N
Ximag=[0]*N
print "Do you want real or integer or complex signal\n\t enter 1 for real, 2 for integer,3 for complex";
ch=int(raw_input())
for i in xrange(N):
	if(ch==3):
		Xreal[i]=random.uniform(-10.0,10.0)
		Ximag[i]=random.uniform(-10.0,10.0)
	elif(ch==2):
		Xreal[i]=int(random.uniform(-10,10))
		Ximag[i]=0
	elif(ch==1):
		Xreal[i]=random.uniform(-10,10)
		Ximag[i]=0
		
zreal=[0]*N
zimag=[0]*N
w=(2*math.pi)/N
for i in xrange(N):
	for j in xrange(N):
		zreal[i]+=(Xreal[j]*math.cos(w*i*j)-Ximag[j]*math.sin(w*i*j))
		zimag[i]+=(Ximag[j]*math.cos(w*i*j)+Xreal[j]*math.sin(w*i*j))
	zreal[i]=zreal[i]/N
	zimag[i]=zimag[i]/N
	

print "\n\nX[n] generated is :"
for i in xrange(N):		
	print "(",round(Xreal[i],3),"+",round(Ximag[i],3),"j",")\t",
print "\n\n"
print "IDFT of X[n] i.e. x[n] is :"	
for i in xrange(N):		
	print "(",round(zreal[i],3),"+",round(zimag[i],3),"j",")\t",
print "\n\n\n"

