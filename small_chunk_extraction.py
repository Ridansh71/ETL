### Case-2 Small chunk Extraction

def extract_data_in_chunks(file_path, chunk_size=1000):
    data = pd.read_csv(file_path, chunksize=chunk_size)
    results = []
    for chunk in data:
        results.append(chunk)
    
    return pd.concat(results)
