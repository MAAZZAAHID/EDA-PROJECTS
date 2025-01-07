import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


#impporting the file 
dataset = pd.read_csv("creditcard.csv")

data=pd.DataFrame(dataset)

legit=dataset['Class']==0
fraud=dataset['Class']==1


# ● How many transactions are fraudulent, and how many are legitimate?

tottal_count=dataset['Class'].value_counts()
legit_counts=dataset['Class'].value_counts()[0]
fraud_counts=dataset['Class'].value_counts()[1]

print(f"\nthe legit count is {legit_counts} and the fradulent count is {fraud_counts} ")


# ● What percentage of transactions are fraudulent?
fraud_percentage = (fraud.sum() / len(dataset)) * 100
print("FRAUD DATA % = ",fraud_percentage)

legit_percentage = (legit.sum() / len(dataset)) * 100
print("LEGIT  DATA % = ",legit_percentage)


# print("head \n")
# print(dataset.head())
# print("tail\n")
# print(dataset.tail())

# ● How many rows and columns are in the dataset?

print("\n ROWS  COLUMNS ")
print(dataset.shape)

# ● What are the column names and their data types?
print(dataset.info())

# ● Are there any missing or null values in the dataset?
print("null values in the dataset?\n")

null_val=dataset.isna().sum().sum()
print(null_val)

# ● What are the minimum, maximum, mean, and median values for numerical columns like Amount?
print("\nthe minimum, maximum, mean, and median values\n")
des=dataset["Amount"].describe()
print("\n",des)

# print("unique\n")
# print(dataset.nunique())


maxamount = dataset['Amount'].max()

print("\nMax amount and its class \n")
r = dataset['Amount'] == maxamount
result = dataset[r][['Amount', 'Class']]

print("The max value is", maxamount)
if result['Class'].iloc[0] == 1:
    print("Fraudulent")
else:
    print("the class is Legitimate")


# ● Can we use a heatmap to visualize the correlation between numerical features?
#heatmap corelation
corr= dataset.corr()

sns.heatmap(corr,cmap="coolwarm",linewidths=0.5)  
plt.title("corelation heatmap")
plt.show()

# ● Can we create a bar chart showing the count of fraudulent vs legitimate transactions?

transa_count = dataset['Class']. value_counts()
categories=['legit','fraud']


values =[transa_count.get(0,0),transa_count.get(1,0)]

plt.bar(categories,values,color=['green','red'])
plt.ylabel("Count")
plt.title("Count of Fraudulent vs Legitimate Transactions")
plt.show()


# ● What does the histogram of transaction amounts look like?
#histogram
plt.hist(dataset["Amount"],bins=100,edgecolor='black')
plt.ylabel( "frequency")
plt.xlabel("amount")
plt.title("histogram of trnasaction amount ")
plt.show()

