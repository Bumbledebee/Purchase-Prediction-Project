# Predicting Purchases: Will This View Turn Into a Purchase?

In the advertising and e-commerce world, not all ad views are equal. Some views lead to purchases, while others do not. Predicting whether a view will result in a purchase is a **classification problem**. This project simulates this problem using an e-commerce shopping dataset, where users interact with products by viewing, adding to the cart, or purchasing them.

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
   - Think about handling class imbalance (or not)
   - Many features are categorical (e.g. brand) and will require encoding.
   - Evaluate model performance using precision as the main key perfomance metric.

---

## Objective

The primary goal of this project is to predict whether a product view will lead to a purchase. By leveraging the provided dataset, we aim to:
- Understand the factors influencing purchase decisions.
- Build a robust machine learning model to classify views as likely to result in a purchase or not.
- Address challenges such as class imbalance and categorical feature encoding.


---

## Results

The results of the project will include:
- Insights from EDA, such as the most influential features for predicting purchases.
- A trained machine learning model capable of predicting purchases with high accuracy.
- Visualizations of feature importance and model performance.
- View the presentation [here](https://ironhack.zoom.us/rec/play/2tWYaGRqo53sBbMu3qpEPIwHCnWezFHc5RlUVmH52ES8Gk4iNuhExD4mSYyMEKCu70CIYE21nyHue5y5.CXx1ib9LHS4nk_4K?accessLevel=meeting&canPlayFromShare=true&from=share_recording_detail&continueMode=true&componentName=rec-play&originRequestUrl=https%3A%2F%2Fironhack.zoom.us%2Frec%2Fshare%2FOjEPsV_L498UWM7OnZRwYYOm-IFCkvU-FV0bsqcB4tX2HZEYqncnU4voeEjTfhs9.MNujQnKc7jLoyQnK) from 2h and 36 Minutes. The presentation is around 10 minutes long.

---

## Future Work

- Explore deep learning models for improved performance.

---

## Authors

- **Debora Bimbi**   
  April 2025