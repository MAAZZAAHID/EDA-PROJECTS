# Credit Card Fraud Detection: Exploratory Data Analysis

This project performs an exploratory data analysis (EDA) on the `creditcard.csv` dataset to investigate the characteristics of credit card transactions and identify fraudulent ones. The dataset contains transaction information, including transaction amount and a binary `Class` column indicating whether a transaction is legitimate (`0`) or fraudulent (`1`).

---

## Features of the Code

### 1. **Dataset Overview**
The dataset is loaded into a pandas DataFrame for analysis. Basic information such as the number of rows, columns, column names, and data types is displayed using:

```python
print(dataset.info())
```

### 2. **Class Distribution**
The script calculates the total number of legitimate and fraudulent transactions:

```python
tottal_count = dataset['Class'].value_counts()
legit_counts = dataset['Class'].value_counts()[0]
fraud_counts = dataset['Class'].value_counts()[1]
```

The percentage of fraudulent and legitimate transactions is computed:

```python
fraud_percentage = (fraud.sum() / len(dataset)) * 100
legit_percentage = (legit.sum() / len(dataset)) * 100
```

### 3. **Dataset Shape**
The total number of rows and columns is printed to understand the size of the dataset:

```python
print(dataset.shape)
```

### 4. **Missing Values Check**
The script verifies if there are any missing or null values in the dataset:

```python
null_val = dataset.isna().sum().sum()
```

### 5. **Statistical Summary**
For the `Amount` column, the script calculates the minimum, maximum, mean, and median values using:

```python
des = dataset["Amount"].describe()
```

### 6. **Maximum Transaction Analysis**
The maximum transaction amount and whether it is fraudulent or legitimate are identified:

```python
maxamount = dataset['Amount'].max()
r = dataset['Amount'] == maxamount
result = dataset[r][['Amount', 'Class']]
```

### 7. **Correlation Heatmap**
A heatmap is generated to visualize the correlation between numerical features:

```python
sns.heatmap(corr, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
```

### 8. **Bar Chart: Fraudulent vs Legitimate Transactions**
A bar chart displays the counts of legitimate and fraudulent transactions:

```python
categories = ['legit', 'fraud']
values = [transa_count.get(0, 0), transa_count.get(1, 0)]
plt.bar(categories, values, color=['green', 'red'])
```

### 9. **Histogram of Transaction Amounts**
A histogram visualizes the distribution of transaction amounts:

```python
plt.hist(dataset["Amount"], bins=100, edgecolor='black')
```



## Output Highlights

- **Class Distribution**: The counts and percentages of fraudulent and legitimate transactions.
- **Missing Values**: A summary confirming no null values in the dataset.
- **Statistical Insights**: Descriptive statistics for the `Amount` column.
- **Visualizations**: Correlation heatmap, bar chart for class distribution, and histogram for transaction amounts.

---

## Conclusion
This project provides an in-depth exploratory analysis of credit card transactions, highlighting the imbalance between fraudulent and legitimate transactions. The visualizations and statistics offer insights into the dataset’s structure, aiding further steps like data preprocessing and building predictive models for fraud detection.


