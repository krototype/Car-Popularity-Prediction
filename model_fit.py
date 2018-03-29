# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 23:12:14 2018

@author: hp
"""

import pandas as pd
import matplotlib.pyplot as plt

#importing the dataset
train=pd.read_csv("train.csv")
test=pd.read_csv("test.csv",names=columns)

columns=['buying_price','maintainence_cost','number_of_doors','number_of_seats','luggage_boot_size','safety_rating']

#fitting the model
from sklearn import svm
X=train[columns]
y=train.popularity
clf=svm.SVC(kernel="rbf",C=300)
clf=clf.fit(X,y)
pred=clf.predict(test[columns])

#preparing the csv file
submission_df={"0":pred}
submission=pd.DataFrame(submission_df)
submission.to_csv("prediction.csv",index=False,header=False)
