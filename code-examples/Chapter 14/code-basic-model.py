# Importing necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load the historical sales data
sales_data = pd.read_csv('sales_data.csv')

# Perform one-hot encoding for categorical variables
sales_data = pd.get_dummies(sales_data, columns=['promotion', 'weather'])

# Preprocessing the data
# Assuming the sales_data.csv contains columns: 'store_id', 'product_id', 'date', 'sales', 'promotion', 'weather', etc.
# Data preprocessing steps such as handling missing values, encoding categorical variables, etc., would be performed here.

# Feature Engineering
# Extracting relevant features from the data
sales_data['date'] = pd.to_datetime(sales_data['date'])
sales_data['day_of_week'] = sales_data['date'].dt.dayofweek
sales_data['month'] = sales_data['date'].dt.month
sales_data['year'] = sales_data['date'].dt.year
# Other relevant features can be extracted based on the specific use-case

# Splitting the data into training and testing sets
X = sales_data.drop(['sales', 'date'], axis=1)
y = sales_data['sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Building the AI model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Making predictions
y_pred = model.predict(X_test)

# Evaluating the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Deploying the model
# Once satisfied with the model's performance, it can be deployed into production for generating demand forecasts in real-time.
# Continuous monitoring and updating of the model would be required to ensure its accuracy and reliability over time.
