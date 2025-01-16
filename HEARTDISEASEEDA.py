import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt


data = pd.read_csv(r"C:\Users\AVACADOO\Desktop\HEART D\heart_disease.csv")

print(data.head())
#How many rows and columns are in the dataset?
rows, columns = data.shape

print(f"no of rows are {rows}")
print(f"no of columns are {columns}")

#Are there any missing values in the dataset?

print("null values in datset")

mising=data.isnull().sum().sum()
if mising > 0:
    print(mising)
else:
    print("no null value")
    
    
#What are the average and median values of:
    
des=data.describe() 
print(des)   



# target distribution 
# Combine all non-zero 'num' values into a single category
data['binary_num'] = data['num'].apply(lambda x: 1 if x > 0 else 0)


binary_target_distribution = data['binary_num'].value_counts()


print("Binary Target Distribution:")
print(binary_target_distribution)

# Plot  distribution
ax = binary_target_distribution.plot(kind='bar', color=['darkblue','lightblue'], edgecolor='black')
plt.title('Distribution of Binary Target Variable')
plt.xlabel("Presence of Heart Disease [0 = No] | [1 = Yes]")
plt.ylabel('Counts')
plt.xticks(rotation=0)

# Add text annotations for counts
for i, count in enumerate(binary_target_distribution):
    plt.text(i, count + 10, str(count), ha='center', va='bottom')

plt.show()


#How many patients have heart disease, and how many don’t?

nodisease=data[data['num']==0]
withdisease=data[data['num']==1]

print(f"patients with no heart disease {nodisease.count()}")
print(f"patients with heart disease {withdisease.count()}")


# age distribution

minage=data['age'].min()
maxage=data['age'].max()

print(f"the min age is {minage} and {maxage} is maximum age of patients in dataset ")


plt.figure(figsize=(12, 6))
age_counts = data['age'].value_counts()

sns.barplot(x=age_counts.index, y=age_counts.values)
plt.xlabel("Age")
plt.ylabel("Age Count")
plt.title("Age Analysis")
plt.show()

# age range of patients

young =data[data['age']>40]
mid = data[(data['age'] > 40) & (data['age'] < 55)]
old=data[data['age']>55]
sns.barplot(x=['28-40','40-55','above 55'], y=[len(young),len(mid),len(old)])
plt.xlabel("age range")
plt.ylabel("age count")
plt.title("age range visualization")
plt.show()

# gender distribution

males=data[data['sex']=='Male'].shape[0]
female=data[data['sex']=='Female'].shape[0]

print(f"no fo males are {males} and no of females are {female}")
plt.hist(data['sex'],bins=3,color='skyblue',edgecolor='black')
plt.title("patients age distribution")
plt.xlabel("GENDER")
plt.ylabel("FREQUENCY")
plt.show()

#How many patients have exercise-induced angina (exang)?
exercise_induceangina=data[data['exang']==1].shape[0]
print(f"pateints with exercise-induced angina = {exercise_induceangina}")
# What are the counts of different chest pain types (cp)?
cpcount=data['cp'].value_counts()
print(f"count of patients with diff chest pains = {cpcount}")

#Compare the average cholesterol levels between patients with and without heart disease.

cholpos=data[data['num']==1]['chol'].mean()
cholnoheart=data[data['num']==0]['chol'].mean()

print(f"the avg pateints with heart disease and chol = {cholpos} and pateints with chol but no heart disease = {cholnoheart}")
 
counts = data.groupby('num')['chol'].mean()

plt.figure(figsize=(8, 4))
counts.plot(kind='bar', color=['skyblue'])
plt.title("Average Cholesterol Levels ACCORDING TO  Heart Disease ")
plt.xlabel("Heart Disease ")  
plt.ylabel("Average Cholesterol")
plt.xticks(rotation=0)
plt.show()


#● Are there any outliers in cholesterol (chol) or resting blood pressure (trestbps)?

for col in ['chol', 'trestbps']:
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    iqr = Q3 - Q1
    lower_bound = Q1 - 1.5 * iqr
    upper_bound = Q3 + 1.5 * iqr
    outliers = data[(data[col] < lower_bound) | (data[col] > upper_bound)]
    print(f"{col}: {len(outliers)} outliers")

sns.boxplot(data=data[['chol', 'trestbps']], palette="Set2")
plt.title("Outliers in Cholesterol and Resting Blood Pressure")
plt.show()
