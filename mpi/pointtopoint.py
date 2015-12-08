
import numpy as np
from mpi4py import MPI

#A = np.arange(0,10000,0.01).reshape((1000,1000))
#print A
#B= A.transpose()
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
lis=[]
while(rank == 0):
	A = np.arange(0,10000,0.01).reshape((1000,1000))
	B=A.transpose()
	print np.linalg.det(A)
	print np.linalg.det(B)
	h0=np.dot(A[0:100,:],B)
        start=100
        stop= 200
        for k in range(9):
                comm.send(A[start:stop, :], dest = k+1, tag =11)
		comm.send(B, dest=k+1, tag=11)
                start=stop
                stop=stop+100
	break
        #for jj in range(9)
               # comm.recv(source=jj+1,tag=11+jj+1)
	#h0=comm.recv(source=0,tag=11)
	#print h0
	#f=h0.ravel
	#lis.append(f)
while( rank==1):
		
	A=comm.recv(source=0,tag=11)
        B=comm.recv(source =0, tag =11)
        print "I am rank %d" %rank
        C = np.dot(A,B)
	print C
	break
while( rank==2):

        A=comm.recv(source=0,tag=11)
        B=comm.recv(source =0, tag =11)
        print "I am rank %d" %rank
        C = np.dot(A,B)
        print C
	break
while(rank==3):

        A=comm.recv(source=0,tag=11)
        B=comm.recv(source =0, tag =11)
        print "I am rank %d" %rank
        C = np.dot(A,B)
        print C
	break
while(rank==4):

        A=comm.recv(source=0,tag=11)
        B=comm.recv(source =0, tag =11)
        print "I am rank %d" %rank
        C = np.dot(A,B)
        print C
	break
while(rank==5):

        A=comm.recv(source=0,tag=11)
        B=comm.recv(source =0, tag =11)
        print "I am rank %d" %rank
        C = np.dot(A,B)
        print C
	break
while(rank==6):

        A=comm.recv(source=0,tag=11)
        B=comm.recv(source =0, tag =11)
        print "I am rank %d" %rank
        C = np.dot(A,B)
        print C
	break
while(rank==7):

        A=comm.recv(source=0,tag=11)
        B=comm.recv(source =0, tag =11)
        print "I am rank %d" %rank
        C = np.dot(A,B)
        print C
	break
while(rank==8):

        A=comm.recv(source=0,tag=11)
        B=comm.recv(source =0, tag =11)
        print "I am rank %d" %rank
        C = np.dot(A,B)
        print C
	break
while(rank==9):

        A=comm.recv(source=0,tag=11)
        B=comm.recv(source =0, tag =11)
        print "I am rank %d" %rank
        C = np.dot(A,B)
        print C
	break

while( rank!=0): 
	comm.send(C, dest=0, tag=5)
	break
else:
	h1 = comm.recv(source=1, tag = 5)
	h2 = comm.recv(source=2, tag = 5)
	h3 = comm.recv(source=3, tag = 5)
	h4 = comm.recv(source=4, tag = 5)
	h5 = comm.recv(source=5, tag = 5)
	h6 = comm.recv(source=6, tag = 5)
	h7 = comm.recv(source=7, tag = 5)
	h8 = comm.recv(source=8, tag = 5)
	h9 = comm.recv(source=9, tag = 5)
	res = np.vstack((h0, h1, h2, h3, h4, h5, h6, h7, h8, h9))
	print res
	print np.linalg.det(res)
