### Case-3 MultiThreaded Extarction


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
