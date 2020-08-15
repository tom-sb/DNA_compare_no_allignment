import math

class Pdist:
	def __init__(self, in_matrix,metric=1):
		self.matrix = in_matrix
		self.vector = self.getVectorDist(metric) 
		#self.euclidean = self.euclideanDist()
	
	def euclideanDist(self, vecA, vecB):
		suma=0
		for i in range(len(vecA)):
			suma += math.pow(vecA[i]-vecB[i],2)
		return math.sqrt(suma)
	
	def getVectorDist(self,metric):
		n = len(self.matrix)
		vecDist = []
		for i in range(n-1):
			for j in range(i+1,n):
				if metric == 1:	
					#vecDist.append([i,j,self.euclideanDist(self.matrix[i], self.matrix[j])])
					vecDist.append(self.euclideanDist(self.matrix[i], self.matrix[j]))
		return vecDist
	
