import scipy.io as sio;
import numpy as np;
import scipy as sp;
"""
Content Analyzer is responsible for converting raw data into tf-idf feature vector.
The output file contains a matrix whose rows are articles , columns are terms.
This format is convenient for ProfileLearner to learn user's interest in the stage 1.
Later, for scalability, I will change the output format.
"""

class ContentAnalyzer:
	tfMatrix=[];  #Scipy matrix instance
	dfVector=[];  #List of df
	N=0;           #Total count of articles
	tcount=0;    #Total count of terms
	maxtfVector=[]; #Max term frequency of each article.

	def __init__(self,tfmatpath,dftxtpath):
		self.loaddata(tfmatpath,dftxtpath);

	def loaddata(self,tfmatpath,dftxtpath):
		data=sio.loadmat(tfmatpath);
		self.tfMatrix = data['fea'];
		self.N,self.tcount = self.tfMatrix.shape;
		print self.N,self.tcount;
		for i in range(10):
			print "process ",i;
			maxv=0;
			for j in range(self.tcount):
				if(self.tfMatrix[i,j]>maxv):
					maxv = self.tfMatrix[i,j];
			self.maxtfVector.append(maxv);

		dfFile = open(dftxtpath,"r");
		for line in dfFile:
			words = line.split();
			self.dfVector.append(int(words[1]));
	
	def dumpstats(self):
		print self.tfMatrix.shape;
		print len(self.dfVector);
		print self.N,self.tcount;
		print len(self.maxtfVector);

	def constructItemVector(self,outputfile):
		mat = sp.sparse.lil_matrix(self.tfMatrix);
		for i in range(10):
			print "Constructing "
			mat[i,:]/=self.maxtfVector[i];
			for j in range(self.tcount):
				scalar = np.log2(self.N/self.dfVector[j]);
				mat[i,j] *=scalar;
			z=mat[i,:].sum();
			mat[i,:]/=z;
		d={'items':mat};

		sio.savemat(outputfile,d);



	

def main():
	ca = ContentAnalyzer('./data/20Newsgroups.mat','./data/AllFeature.txt');
	ca.dumpstats();
	ca.constructItemVector('./data/ItemVectors_out.mat');


if __name__ == "__main__":
	main();


