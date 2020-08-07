from Bio import SeqIO
import numpy as np
from matplotlib import pyplot as plt

class Seqpicture:

	def __init__(self, path):
		self.alpha = {'AA':1,'AG':17,'AC':34,'AT':51,'GA':68,'GG':85,'GC':102,'GT':119,'CA':136,'CG':153,'CC':170,'CT':187,'TA':204,'TG':221,'TC':238,'TT':255}
		self.picture = self.makePic(path)

	def makePic(self, path):
		data = self.datacleaning(path)
		matrix = [[] for i in range(len(data)//70)]
		it = 0
		for row in range(len(data)//70):
			for col in range(70):
				if it+1 == len(data):
					break
				if it != (70*(row+1))-1:
					pair = data[it]+data[it+1]
					matrix[row].append(self.alpha[pair])
				it += 1
		return np.array(matrix)

	def datacleaning(self,path, dtype='fasta'):
		sequences = SeqIO.parse(path,dtype)
		for record in sequences:
			data = str(record.seq.upper())
		return data

mypic = Seqpicture("sequence.fasta")
#plt.imshow(mypic.picture)
#plt.show()
