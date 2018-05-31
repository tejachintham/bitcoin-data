import numpy as np
import sys
from sklearn.cluster import KMeans
import pandas as pd
ls=[]
i=0
sys.argv[0]="pdf.py"
file1 = open(sys.argv[1],"r+")
gh=file1.readlines()
for g in gh:
    ml=g.split(',')
    if(i==1):
        ls.append(ml)
    i=1    
hg=pd.DataFrame(ls)
X=hg.as_matrix()
kmeans = KMeans(n_clusters=int(sys.argv[2])).fit(X)
labels=kmeans.predict(X)
C=kmeans.cluster_centers_
file2 = open("output.txt","w")
for c in C:
    ghf=str(c)
    file2.write(ghf)
    file2.write("\n")
file2.close()

