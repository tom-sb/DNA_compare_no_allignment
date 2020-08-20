from fastopic import Seqpic
from toolstat import Statpic
from mypdist import Pdist
import os
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt

import pandas as pd
from sklearn.decomposition import PCA
import numpy as np


fastaFile = input('ingreser nombre de archivo contenedor de archivos .fasta: ')+'/'
outpath = "out"+fastaFile
##############################
with os.scandir() as itr: 
	findin = False
	findout = False
	for entry in itr :
		if entry.name+'/' == fastaFile:
			#arr = sorted(os.listdir(fastaFile))
			arr = os.listdir(fastaFile)
			findin = True
		if entry.name+'/' == outpath:
			findout = True
	if findout == False:
		os.mkdir(outpath)
	if findin == False:
		print('error al ingresar directorio, "'+fastaFile+'" no existe, ingrese un directorio q exista.')
		raise SystemExit
###############################

#arr = sorted(os.listdir(fastaFile))
print(arr)

n = len(arr)
picarr=[]
labelarr=[]

for i in range(n):
	picarr.append(Seqpic(fastaFile+arr[i],outpath))

statarr = []
statarr2 = []
for i in range(n):
	#picarr[i].picShow()
	#picarr[i].histShow()
	labelarr.append(picarr[i].title)
	stat = Statpic(picarr[i])
	statarr.append(stat.makeVecFeatures())

print("##############################################")
print("vectores de caracteristicas")
print("minskowski distance r1")
for i in range(n):
	print(statarr[i])

pdist = Pdist(statarr)
vec = pdist.vector
vecid = pdist.vectorId
print("##############################################")
print("Indice  ---  nombres")
for i in range(n):
	print(i," , ",labelarr[i])
print("##############################################")
print("matriz triangular de similitus aqui abajo")
print(vecid)
newvec = pdist.getVsAll(3)
print(newvec)

"""
############# PCA ####
#print(statarr)
X=statarr
columns=['a','b','c','d']#X.columns.values
pca=PCA(n_components=2)
pca.fit(X)
pca_values=pca.components_
plt.figure(figsize=(10,10))
plt.rcParams.update({'font.size':14})
x=np.linspace(start=-1,stop=1,num=500)
y_positive=lambda x: np.sqrt(1-x**2)
y_negative=lambda x: -np.sqrt(1-x**2)
plt.plot(x,list(map(y_positive,x)),color='blue')
plt.plot(x,list(map(y_negative,x)),color='blue')
x=np.linspace(start=-0.5,stop=0.5,num=500)
y_positive=lambda x: np.sqrt(0.5**2-x**2)
y_negative=lambda x: -np.sqrt(0.5**2-x**2)
plt.plot(x,list(map(y_positive,x)),color='green')
plt.plot(x,list(map(y_negative,x)),color='red')
x=np.linspace(start=-1,stop=1,num=30)
plt.scatter(x,[0]*len(x),marker='_',color='maroon')
plt.scatter([0]*len(x),(x),marker='|',color='maroon')
colors=['blue','red','green','black','purple','brown']
if len(pca_values[0])>6:
	colors=color*(int(len(pca_values[0])/6)+1)
add_string=""
for i in range(len(pca_values[0])):
	xi=pca_values[0][i]
	yi=pca_values[1][i]
	plt.arrow(0,0,dx=xi,dy=yi,head_width=0.03,head_length=0.03,color=colors[i],length_includes_head=True)
	add_string=f"({round(xi,2)}{round(yi,2)})"
	plt.text(pca_values[0,i],pca_values[1,i],s=columns[i]+add_string)
plt.xlabel(f"Component1({round(pca.explained_variance_ratio_[0]*100,2)}%)")
plt.ylabel(f"Component2({round(pca.explained_variance_ratio_[1]*100,2)}%)")
plt.title('Variable factor map (PCA)')
plt.show()

######################
"""


Z=linkage(vec,'average')
#Z2=linkage(statarr,'single',metric='euclidean')

fig = plt.figure(figsize=(25,10))
dn = dendrogram(Z,orientation='left',labels=labelarr)
fig.tight_layout()
fig.savefig(fastaFile[:len(fastaFile)-1]+'dendrogram.png')
plt.show()
#dn2 = dendrogram(Z2)
#plt.show()

