import numpy as np
from mpi4py import MPI
comm=MPI.COMM_WORLD

rank=comm.Get_rank()
if rank==0:
	A=np.arange(0,10000,0.01).reshape((1000,1000)) 
	B=A.transpose()
	lis=[]
	start=0
	stop=100
	for ii in range(10):	
		cc=A[start:stop,:]
		#cc=cc.ravel()
		lis.append(cc)
		start=stop
		stop=stop+100
	print len(lis)

	Aa=np.arange(0,10000,0.01)
else:
	A=None
	B=None
	lis=None
B=comm.bcast(B,root=0)
A1=comm.scatter(lis,root=0)
#A1=np.array(A1)
#A1=A1.reshape((100,1000))
C=np.dot(A1,B)
print C
res=comm.gather(C,root=0)
print res
#C=np.dot(A,B)
#comm.Barrier()
#res=comm.gather(C,root=0)
if rank==0:
	res1=np.array(res).reshape((1000,1000))
	#res=res.reshape((1000,1000))
	print np.linalg.det(res1)
