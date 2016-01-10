
#A= [10,1,2,8,5,20]
A= [10,50,5,1]
def solution(A):
	for i in range(0,len(A)):
		for j in range(0,len(A)):
			if A[i] < A[j]:
				z=A[j]
				A[j]=A[i]
				A[i]=z
			
	for i in range(0,len(A)-2):
		sum1=A[i]+A[i+1]
		if sum1 > A[i+2]:
			return 1
	return 0		
		
			
