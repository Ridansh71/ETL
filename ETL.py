#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import numpy as np
import concurrent.futures
import time
from sklearn.preprocessing import MinMaxScaler


# # Extract Part

# In[3]:


retail = pd.read_csv('Features data set.csv')


# In[4]:


retail.head()


# In[5]:


retail.shape


# # Transform Part

# In[6]:


retail.dtypes


# In[20]:


#Transformations to make the data more consistent

retail['Date'] = pd.to_datetime(retail['Date'],format="%d/%m/%Y")

# Fill missing values with 0
retail.fillna(0, inplace=True)

# Normalize numeric columns
scaler = MinMaxScaler()
numeric_columns = ['Temperature', 'Fuel_Price', 'MarkDown1', 'MarkDown2', 'MarkDown3', 'MarkDown4', 'MarkDown5', 'CPI', 'Unemployment']
retail[numeric_columns] = scaler.fit_transform(retail[numeric_columns])


# Convert IsHoliday to integer
retail['IsHoliday'] = retail['IsHoliday'].astype(int)


# In[16]:


retail.head()


# ### Creating sample datasets 

# In[42]:


# Function to create a sample dataset
def create_dataset(num_rows):
    np.random.seed(0)
    start_date = pd.Timestamp('2020-01-01')
    end_date = pd.Timestamp('2023-12-31')
    date_range = pd.date_range(start=start_date, end=end_date, periods=num_rows)
    
    data = {
        'Store': np.random.randint(1, 50, num_rows),
        'Date': date_range,
        'Temperature': np.random.uniform(30, 100, num_rows),
        'Fuel_Price': np.random.uniform(2, 4, num_rows),
        'MarkDown1': np.random.uniform(0, 1000, num_rows),
        'MarkDown2': np.random.uniform(0, 1000, num_rows),
        'MarkDown3': np.random.uniform(0, 1000, num_rows),
        'MarkDown4': np.random.uniform(0, 1000, num_rows),
        'MarkDown5': np.random.uniform(0, 1000, num_rows),
        'CPI': np.random.uniform(100, 200, num_rows),
        'Unemployment': np.random.uniform(4, 10, num_rows),
        'IsHoliday': np.random.choice([True, False], num_rows)
    }
    return pd.DataFrame(data)

# Create and save datasets of different sizes
sizes = [10000, 100000, 1000000]
for size in sizes:
    dataset = create_dataset(size)
    dataset.to_csv(f'data_{size}.csv', index=False)


# ## Case-1 Row by Row Extraction

# In[29]:


def extract_data_row_by_row(file_path):
    data = pd.read_csv(file_path)
    return data


# ## Case-2 Small chunk Extraction

# In[45]:


def extract_data_in_chunks(file_path, chunk_size=1000):
    data = pd.read_csv(file_path, chunksize=chunk_size)
    results = []
    for chunk in data:
        results.append(chunk)
    
    return pd.concat(results)


# ## Case-3 MultiThreaded Extarction

# In[1]:


# Data Processing Function
def process_data(data):
    data.fillna(0, inplace=True)  # Fill missing values with 0
    return data

# Multi-threaded Extraction
def extract_data_multithreaded(file_path, chunk_size=1000):
    data = pd.read_csv(file_path, chunksize=chunk_size)
    results = []
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_data, chunk) for chunk in data]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
    
    return pd.concat(results)


# In[46]:


# Benchmarking Each Method
file_paths = ['data_10000.csv', 'data_100000.csv', 'data_1000000.csv']

for file_path in file_paths:
    print(f"Testing with {file_path}")
    
    start_time = time.time()
    data_multithreaded = extract_data_multithreaded(file_path)
    processed_data_multithreaded = process_data(data_multithreaded)
    end_time = time.time()
    print(f"Multi-threaded execution time: {end_time - start_time} seconds")

    start_time = time.time()
    data_row_by_row = extract_data_row_by_row(file_path)
    processed_data_row_by_row = process_data(data_row_by_row)
    end_time = time.time()
    print(f"Row-by-row execution time: {end_time - start_time} seconds")

    start_time = time.time()
    data_chunks = extract_data_in_chunks(file_path)
    processed_data_chunks = process_data(data_chunks)
    end_time = time.time()
    print(f"Chunk-based execution time: {end_time - start_time} seconds")
    print()


# In[52]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Data 
data = {
    'Method': ['Multi-threaded', 'Row-by-row', 'Chunk-based'],
    'Size_10000': [0.08101, 0.0469, 0.0789],
    'Size_100000': [0.5559, 0.2200, 0.6070],
    'Size_1000000': [5.615, 1.9639, 5.6124]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Melt the DataFrame to long format for easier plotting
df_melted = df.melt(id_vars='Method', var_name='Dataset Size', value_name='Execution Time (seconds)')

# Plotting with Seaborn
plt.figure(figsize=(12, 10))
sns.barplot(x='Dataset Size', y='Execution Time (seconds)', hue='Method', data=df_melted, palette='Set2')
plt.title('Execution Times for Different Data Processing Methods')
plt.xlabel('Dataset Size')
plt.ylabel('Execution Time (seconds)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[51]:


data = {
    'Method': ['Multi-threaded', 'Row-by-row', 'Chunk-based'],
    'Size_10000': [0.08101, 0.0469, 0.0789],
    'Size_100000': [0.5559, 0.2200, 0.6070],
    'Size_1000000': [5.615, 1.9639, 5.6124]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Melt the DataFrame to long format for easier plotting
df_melted = df.melt(id_vars='Method', var_name='Dataset Size', value_name='Execution Time (seconds)')

# Plotting with Seaborn
plt.figure(figsize=(12, 10))
sns.lineplot(x='Dataset Size', y='Execution Time (seconds)', hue='Method', data=df_melted, marker='o', palette='Set1')
plt.title('Execution Times for Different Data Processing Methods')
plt.xlabel('Dataset Size')
plt.ylabel('Execution Time (seconds)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

