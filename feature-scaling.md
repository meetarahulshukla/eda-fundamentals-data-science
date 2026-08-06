# Feature Scaling Fundamentals

Scaling, specifically feature scaling, is a critical preprocessing step in machine learning used to normalise the ranges of independent variables. Since features often have vastly different scales (e.g., age vs. annual income), scaling ensures that no single feature dominates the model's objective function simply due to its magnitude.

---

## 1. Primary Scaling Methodologies

### Standardisation (Z-score Normalisation)
* **Process:** Transforms the data so that it has a mean of `0` and a standard deviation of `1`.
* **Use Case:** Highly effective for features that follow a normal distribution or for algorithms that assume Gaussian-distributed data.
* **Implementation:** Handled via `StandardScaler` from the `sklearn.preprocessing` library.

### Normalisation (Min-Max Scaling)
* **Process:** Scales the values of a feature to a fixed, bounded range (typically `0` to `1`).
* **Use Case:** Used to bound features with differing scales to a uniform range without necessarily changing the distribution's shape.
* **Implementation:** Handled via `MinMaxScaler` from the `sklearn.preprocessing` library.

---

## 2. Why Scaling Matters

Scaling is essential for the performance, stability, and convergence of specific model families:

* **Distance-Based Models:** Algorithms like K-Nearest Neighbors (KNN) and Support Vector Machines (SVM) rely on distance metrics (e.g., Euclidean distance). Unscaled features with larger numerical ranges will disproportionately dominate the distance calculation.
* **Gradient Descent Models:** Models like Linear Regression, Logistic Regression, and Neural Networks use gradient descent. Scaling ensures a symmetric error surface, helping the algorithm converge faster and more reliably.

---

## 3. When to Skip Scaling

Scaling is not universally required across all machine learning architectures:

* **Tree-Based Models:** Algorithms like Decision Trees, Random Forests, and Gradient Boosting (XGBoost, LightGBM) are scale-invariant. They split nodes based on relative feature ordering rather than absolute values, meaning scaling will not change their performance.
