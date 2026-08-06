# Exploratory Data Analysis (EDA) Fundamentals

**Exploratory Data Analysis (EDA)** is the process of analysing and summarising datasets to uncover patterns, detect anomalies, and validate assumptions. It forms the **bedrock of data science projects**, ensuring accurate model selection, preventing incorrect conclusions, and identifying data distributions before formal modelling begins.

---

## 1. Core Objectives and Steps
The primary goal of EDA is to discover insights through a structured process:

* **Data Collection:** Gathering raw data from various sources like APIs, CSVs, or databases.
* **Data Cleaning:** Addressing missing values, removing duplicates, and standardising formats to prevent data distortion.
* **Data Profiling:** Reviewing summary statistics and feature distributions to assess data quality and identify inconsistencies.
* **Data Visualisation:** Using charts to recognise patterns, trends, and skewness.

---

## 2. Understanding Data Characteristics
A critical part of EDA is identifying **data types**, as they dictate the appropriate statistical methods and visualisations:

* **Numerical Variables:** Categorised as continuous or discrete; analysed using measures like **mean, median, mode** (central tendency) and **variance or standard deviation** (dispersion).
* **Categorical Variables:** Categorised as nominal or ordinal; often requires encoding (label or one-hot) for model compatibility.

---

## 3. Outlier Detection and Management
EDA is vital for detecting outliers that could skew distributions and disrupt machine learning algorithms. Key techniques include:

* **Z-Score Method:** Measures how many standard deviations a point is from the mean; values typically above 3 or below -3 are flagged.
* **Interquartile Range (IQR):** Identifies outliers as values falling beyond 1.5 times the range between the 25th (Q1) and 75th (Q3) percentiles.
* **Visual Identification:** **Box plots** provide a clear view of medians and quartiles with "whiskers" showing the spread, while **scatter plots** reveal points far from the main data cluster.

---

## 4. Advanced Visualisation and Multivariate Analysis
Moving beyond basic summaries, advanced EDA explores complex relationships within the data:

* **Multivariate EDA:** Tools like **Pairplots** visualise relationships between multiple features simultaneously to reveal clusters or separation between classes.
* **Correlation Heatmaps:** Use a color-coded matrix to measure the strength and direction of linear relationships between variables, helping identify redundant features.
* **Target-Wise EDA:** Compares features against the target variable (e.g., survival in the Titanic dataset) using boxplots for numeric data or bar plots for categorical data to extract predictive insights.

---

## 5. Tools for EDA
Effective exploration relies on specific Python libraries:

* **Pandas:** Essential for data manipulation and basic filtering.
* **Matplotlib & Seaborn:** Used for creating a wide array of visualisations from histograms to complex heatmaps.
* **Automated EDA Tools:** Libraries like **ydata-profiling** and **Sweetviz** can generate rapid HTML reports with instant summaries of distributions and missing values, though they should supplement rather than replace expert judgment.
