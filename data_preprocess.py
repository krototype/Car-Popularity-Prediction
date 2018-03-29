# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 23:03:39 2018

@author: hp
"""

import pandas as pd
import matplotlib.pyplot as plt
train=pd.read_csv("train.csv")

#barplot of popularity
fig=plt.figure()
ax = fig.add_subplot(1,1,1)
ax.hist(train.popularity,bins = 7)
plt.title('car popularity')
plt.xlabel('popularity')
plt.ylabel('cars')
plt.show()

#train_description
train.describe()

#boxplot of popularity
figure1=plt.figure()
bx=figure1.add_subplot(1,1,1)
bx.boxplot(train.popularity)
plt.ylabel('popularity')
plt.show()

columns=['buying_price','maintainence_cost','number_of_doors','number_of_seats','luggage_boot_size','safety_rating']

#getting all relationship plots
for i in columns:
    fig2=plt.figure()
    ax=fig2.add_subplot(111)
    ax.scatter(train[i],train.popularity,color='grey',alpha=0.05)
    plt.ylabel('popularity')
    plt.xlabel(i)
    plt.show()
    
#checking for the null values
for i in columns:
    print(i)
    print(train[i].isnull().sum())