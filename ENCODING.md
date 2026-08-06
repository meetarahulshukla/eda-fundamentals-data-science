# Categorical Encoding and Data Transformation Fundamentals

Encoding is a fundamental feature engineering process used to convert categorical data into a numeric form so it can be processed by machine learning models. Because most algorithms require numerical inputs to perform statistical calculations, encoding ensures that categorical information—such as gender, location, or rank—is accurately represented.

---

## 1. Key Encoding Strategies

### One-Hot Encoding
* **Definition:** Creates a new binary column for each category in a feature. For example, if a column "Embarked" has three cities, it will be split into three columns, where a `1` indicates the presence of that category and `0` indicates its absence.
* **Best Use Case:** Highly effective for nominal data (categories without a natural order). Recommended for use with tree-based and linear models.
* **Implementation:** Achieved in Python using `pd.get_dummies()` or Scikit-Learn’s `OneHotEncoder`.

### Label Encoding
* **Definition:** Maps each unique category to a unique integer (e.g., 0, 1, 2).
* **Best Use Case:** Simple to implement, but caution is required. Label Encoding can introduce an artificial mathematical order where none exists, which may mislead certain linear algorithms.
* **Implementation:** Implemented using Scikit-Learn’s `LabelEncoder`.

### Ordinal Encoding
* **Definition:** Similar to Label Encoding, but specifically applied to ordered levels where the numeric sequence reflects a natural hierarchy.
* **Example:** Mapping levels like "Low," "Medium," and "High" to `0`, `1`, and `2`, or ranking "Bronze," "Silver," and "Gold".

---
