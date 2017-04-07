import pandas as pd
import numpy as np

def ndc2(csv_path,ndc_varname,out):

	df=pd.read_csv(csv_path)
	
	#NDCs have to be in the format 4-4-2, 5-3-2,5-4-1. Should add something to handle that potential error
	s=pd.Series(df[ndc_varname])
	print s
	#Split up the NDC into 3 parts
	df['first']=s.str.split('-',  expand=True).get(0)
	df['second']=s.str.split('-',  expand=True).get(1)
	df['third']=s.str.split('-',  expand=True).get(2)

	#Turn these variables into series so I can manipulate them
	s1=pd.Series(df['first'])
	s2=pd.Series(df['second'])
	s3=pd.Series(df['third'])

	#Grab the length of each variable#
	l1=s1.str.len()
	l2=s2.str.len()
	l3=s3.str.len()
	
	#This is the best logic I can do, test 4-4-2
	x=np.logical_and(l1==4, l2==4)
	y=np.logical_and(l1==4, l3==2)
	z=np.logical_and(l2==4, l3==2)
	T=np.logical_and(np.logical_and(x,y),z)

	new1=np.where(T,("_"+"0"+df['first']+df['second']+df['third']),"")
	
	#test 5-3-2
	x=np.logical_and(l1==5, l2==3)
	y=np.logical_and(l1==5, l3==2)
	z=np.logical_and(l2==3, l3==2)
	T=np.logical_and(np.logical_and(x,y),z)
	
	new2=np.where(T,("_"+df['first']+"0"+df['second']+df['third']),"")
	
	#test 5-4-1
	x=np.logical_and(l1==5, l2==4)
	y=np.logical_and(l1==5, l3==1)
	z=np.logical_and(l2==4, l3==1)
	T=np.logical_and(np.logical_and(x,y),z)
	
	new3=np.where(T,("_"+df['first']+df['second']+"0"+df['third']),"")
	
	#Create the NDC Variable
	df['ndc11'] = new1+new2+new3
	
	df.to_csv(out)

#convertndc11(csv_path="C:/Users/hollands/Documents/Antipsychotics - Marcela/Data/ndc10.csv",ndc_varname='ndcpackagecode',out="C:/Users/hollands/Documents/Antipsychotics - Marcela/NewNDCs.csv")