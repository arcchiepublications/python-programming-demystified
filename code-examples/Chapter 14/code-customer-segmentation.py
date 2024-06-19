# Importing necessary libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the customer data
customer_data = pd.read_csv('customer_data.csv')

# Preprocessing the data
# Assuming the customer_data.csv contains columns: 'customer_id', 'age', 'income', 'transaction_amount', etc.
# Data preprocessing steps such as handling missing values, encoding categorical variables, etc., would be performed here.

# Selecting relevant features for segmentation
X = customer_data[['age', 'income', 'transaction_amount']]

# Standardizing the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determining the optimal number of clusters using the Elbow method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Plotting the Elbow curve
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# Applying KMeans clustering with the optimal number of clusters
k = 3  # Assuming 3 clusters based on the Elbow curve
kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
y_pred = kmeans.fit_predict(X_scaled)

# Adding the cluster labels to the customer data
customer_data['cluster'] = y_pred

# Visualizing the clusters
plt.scatter(X_scaled[y_pred == 0, 0], X_scaled[y_pred == 0, 1], s=100, c='red', label='Cluster 1')
plt.scatter(X_scaled[y_pred == 1, 0], X_scaled[y_pred == 1, 1], s=100, c='blue', label='Cluster 2')
plt.scatter(X_scaled[y_pred == 2, 0], X_scaled[y_pred == 2, 1], s=100, c='green', label='Cluster 3')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label='Centroids')
plt.title('Customer Segmentation')
plt.xlabel('Age')
plt.ylabel('Income')
plt.legend()
plt.show()

# Outputting the segmented customer data
print(customer_data)
