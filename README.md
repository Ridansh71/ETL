# ETL Performance Optimization Project

## Introduction
This project aims to evaluate and compare the performance of different data extraction methods commonly used in ETL (Extract, Transform, Load) processes. Optimizing data extraction is crucial for improving overall ETL pipeline efficiency.

## Dataset Description
The dataset used in this project consists of Store - the store number
Date - the week
Temperature - average temperature in the region
Fuel_Price - cost of fuel in the region
MarkDown1-5 - anonymized data related to promotional markdowns. MarkDown data is only available after Nov 2011, and is not available for all stores all the time. Any missing value is marked with an NA
CPI - the consumer price index
Unemployment - the unemployment rate
IsHoliday - whether the week is a special holiday week. Data is sourced from Kaggle.

## Methodology

### Case 1: Multi-threading
Multi-threading leverages concurrent execution of threads to improve data extraction speed. This section explains the implementation using Python's threading module.

### Case 2: Row-by-Row Extraction
Row-by-row extraction involves iterating through each row sequentially. Discuss the traditional approach, its limitations, and challenges in large-scale data processing.

### Case 3: Small Chunk Extraction
Small chunk extraction involves processing data in manageable batches. This section discusses its benefits in balancing performance and resource usage.

## Implementation
Detailed steps on how each extraction method was implemented are provided in the code files:
- `multi_threading_extraction.py`: Implementation of multi-threaded data extraction.
- `row_by_row_extraction.py`: Implementation of row-by-row data extraction.
- `small_chunk_extraction.py`: Implementation of small chunk data extraction.

## Performance Evaluation
### Metrics
Performance metrics evaluated include:
- **Execution Time:** Measured in seconds.
- **CPU Utilization:** Percentage of CPU resources used during extraction.

### Results
Results of performance tests for each method are summarized and visualized using charts and graphs.

![Performance Comparison Chart](performance_comparison)

## Analysis and Discussion
Analysis of results, including:
- Explanation of performance differences.
- Considerations in choosing the optimal extraction method based on dataset size and system resources.

## Conclusion
Summary of findings and implications for ETL process optimization. Suggestions for future improvements or extensions to the project.

## Appendix
Additional information:
- Full code listings (`multi_threading_extraction.py`, `row_by_row_extraction.py`, `small_chunk_extraction.py`).
- Detailed test results and data used for benchmarking.
