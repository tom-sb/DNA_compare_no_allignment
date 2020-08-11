#ETEtoolkit
from fastopic import Seqpic 
import math 

class Statpic:
	def __init__(self, seqpic):
		#self.prob = self.getProb(seqpic.makeHist(), len(seqpic.picture)) 
		self.prob = self.getProb(seqpic.makeHist(), seqpic.picture.size) 
		self.average = self.getAverage(seqpic.makeHist()) 
		self.variance = self.getVariance(seqpic.makeHist())
		self.desv = math.sqrt(self.variance)
		self.skewness = self.getSkewness(seqpic.makeHist())
		self.kurtosis = self.getKurtosis(seqpic.makeHist())
		self.energy = self.getEnergy()
		self.entropy = self.getEntropy()
	
	def getProb(self, histo,size):
		prob = []
		for i in range(len(histo)):
			prob.append(histo[i][1]/size)	
			print(histo[i][1]/size)	
		return prob

	def getAverage(self, histo):
		average = 0
		for i in range(len(self.prob)):
			average += histo[i][0]*self.prob[i]
		print("average",average)
		return average

	def getVariance(self,histo):
		variance = 0
		for i in range(len(self.prob)):
			variance += pow(histo[i][0]-self.average,2) * self.prob[i]
		print(" variance",variance)
		return variance

	def getSkewness(self,histo):
		skewness = 0
		for i in range(len(self.prob)):
			skewness += pow(histo[i][0]-self.average,3) * self.prob[i]
		skewness = skewness / pow(self.desv,3)
		print("skewness",skewness)
		return skewness

	def getKurtosis(self, histo):
		kurtosis = 0
		for i in range(len(self.prob)):
			kurtosis += pow(histo[i][0]-self.average,4) * self.prob[i] 
		kurtosis =(kurtosis / pow(self.desv,4))-3
		print("kurtosis",kurtosis)
		return kurtosis

	def getEnergy(self):
		energy = 0
		for i in range(len(self.prob)):
			energy += pow(self.prob[i],2)
		print("energy",energy)
		return energy
		
	def getEntropy(self):
		entropy = 0
		for i in range(len(self.prob)):
			entropy += self.prob[i] * math.log(self.prob[i],2)
		print("entropy",entropy*-1)
		return entropy*-1
		
