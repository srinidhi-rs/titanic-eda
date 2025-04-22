# 🚢 Titanic Data Analysis & Visualization (Exploratory Data Analysis)

This project performs **exploratory data analysis (EDA)** on the classic Titanic dataset using **Python**, **Pandas**, **Matplotlib**, and **Seaborn**. The goal is to explore the demographics and survival patterns of the passengers onboard the Titanic.


## 🎯 Project Objective

- To understand the survival patterns among Titanic passengers.
- To perform data cleaning and preprocessing.
- To visualize key features such as age distribution, gender-based survival, and fare distribution.
- To identify patterns and insights that may assist in further machine learning modeling.

---

## 📂 Dataset Description

The Titanic dataset contains information about the passengers onboard the RMS Titanic. Each row represents a passenger, and the features include:

| Column        | Description                                  |
|---------------|----------------------------------------------|
| PassengerId   | Unique identifier for each passenger         |
| Survived      | Survival status (0 = No, 1 = Yes)            |
| Pclass        | Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)      |
| Name          | Full name of the passenger                   |
| Sex           | Gender                                       |
| Age           | Age in years                                 |
| SibSp         | Number of siblings/spouses aboard            |
| Parch         | Number of parents/children aboard            |
| Ticket        | Ticket number                                |
| Fare          | Fare paid for the ticket                     |
| Cabin         | Cabin number                                 |
| Embarked      | Port of Embarkation (C = Cherbourg, Q = Queenstown, S = Southampton) |

---

## 🧹 Data Cleaning & Preprocessing

The dataset required the following cleaning steps:

- **Missing Values**:
  - `Age`: Replaced missing values with the **mean age**.
  - `Cabin`: Replaced missing values with `"Unknown"` due to high sparsity.
  - `Embarked`: Dropped rows with missing embarkation info (only 2 entries).

- **Duplicates**: Verified that there are no duplicated rows.

---

## 📊 Exploratory Data Analysis (EDA)

The EDA focuses on exploring the distribution and relationship of the features:

### 1. Age Distribution
- Visualizes how ages are distributed among passengers.
- Helps identify the population makeup in terms of age groups.

### 2. Survival by Gender
- Shows how gender affected the survival rate.
- Confirms that **females had a higher survival rate** than males.

### 3. Age vs Fare (colored by Survival)
- Identifies whether fare or age had any visible influence on survival.
- Can be used for preliminary feature assessment for machine learning models.

---

## 📈 Visualizations

Here are the main plots generated in this analysis:

- 📌 **Histogram of Age** with KDE overlay
- 📌 **Count Plot** of Gender vs Survival
- 📌 **Scatter Plot** of Age vs Fare, color-coded by survival status

---

## 🛠 Technologies Used

- **Python 3.x**
- **Pandas** – for data manipulation
- **Matplotlib** – for basic plotting
- **Seaborn** – for statistical and categorical visualizations
- **Jupyter Notebook** / **PyCharm** – for interactive analysis
