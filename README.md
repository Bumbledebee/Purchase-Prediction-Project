# Predicting Purchases: Will This View Turn Into a Purchase?

In the advertising and e-commerce world, not all product views are equal. Some views lead to purchases, while others do not. Predicting whether a view will result in a purchase is a **classification problem**. This project simulates this problem using an e-commerce shopping dataset, where users interact with products by viewing, adding to the cart, or purchasing them.

The dataset is highly imbalanced, as only a small fraction of views result in purchases. By splitting the dataset into views that lead to purchases and those that do not, we aim to create a predictive model capable of handling this imbalance.

---

## Data Overview

**Dataset**: `events.csv`  
**Rows**: 885,129  
**Columns**: 9  

### Column Descriptions:
- **event_time**: Timestamp of the event.
- **event_type**: Type of the event, which can be one of the following:
  - `view`: A product was viewed.
  - `cart`: A product was added to the cart.
  - `purchase`: A product was purchased.
- **product_id**: Unique identifier for the product (53,452 unique products).
- **category_id**: Identifier for the product category (718 unique values).
- **category_code**: A hierarchical category code grouped by product ID (108 unique values).
- **brand**: Brand of the product (1,000 unique brands).
- **price**: Continuous numeric column representing the product price.  
  - **Range**: Min: 0.22, Max: 64,771.06 (currency unknown).
- **user_id**: Unique identifier for users (407,283 unique users).
- **user_session**: Identifier for a user's session.

---

## Project Plan

1. **Data Cleaning**:
   - Handle missing values.
   - Format timestamps and categorical data.
   - Normalize and preprocess numerical features.

2. **Explorative Data Analysis (EDA)**:
   - Analyze event distributions (views, carts, purchases).
   - Investigate relationships between features (e.g., price vs. purchase likelihood).
   - Visualize trends and patterns in the data.

3. **Machine Learning**:
   - Build a classification model to predict whether a view will result in a purchase.
   - Handle class imbalance using techniques like oversampling, undersampling, or class weighting.
   - Evaluate model performance using metrics such as precision, recall, F1-score, and ROC-AUC.

---

## Objective

The primary goal of this project is to predict whether a product view will lead to a purchase. By leveraging the provided dataset, we aim to:
- Understand the factors influencing purchase decisions.
- Build a robust machine learning model to classify views as likely to result in a purchase or not.
- Address challenges such as class imbalance and categorical feature encoding.

---

## Tools and Technologies

- **Programming Language**: Python
- **Libraries**:
  - Data Manipulation: `pandas`, `numpy`
  - Visualization: `matplotlib`, `seaborn`
  - Machine Learning: `scikit-learn`
- **Environment**: Jupyter Notebook

---

## Dataset Insights

- The dataset contains **885,129 rows** and **9 columns**.
- The target variable is **last_view_before_purchase**, specifically predicting the transition from `view` to `purchase` as 0 or 1.
- The dataset is highly imbalanced, with a majority of events being `view` and only a small fraction being `purchase`.

---

## Challenges

1. **Class Imbalance**:
   - The dataset is dominated by `view` events, with relatively few `purchase` events. There is a high inherent imbalance.

2. **Categorical Features**:
   - Many features, such as `category_code` and `brand`, are categorical and require encoding.

3. **Scalability**:
   - The dataset is large, requiring efficient preprocessing and modeling techniques.

---

## Results

The results of the project will include:
- Insights from EDA, such as the most influential features for predicting purchases.
- A trained machine learning model capable of predicting purchases with high accuracy.
- Visualizations of feature importance and model performance.

---

## Future Work

- Explore deep learning models for improved performance.

---

## Authors

- **Debora Bimbi**   
  April 2025