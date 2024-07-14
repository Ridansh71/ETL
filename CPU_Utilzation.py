import psutil
import matplotlib.pyplot as plt
import datetime
import time

# Function to get CPU utilization
def get_cpu_utilization():
    return psutil.cpu_percent(interval=1, percpu=True)

# Function to plot CPU utilization
def plot_cpu_utilization(cpu_data, timestamps):
    num_cores = len(cpu_data)
    
    plt.figure(figsize=(12, 6))
    for core in range(num_cores):
        plt.plot(timestamps, cpu_data[core], label=f"Core {core}")
    
    plt.title('CPU Utilization Over Time')
    plt.xlabel('Time')
    plt.ylabel('CPU Utilization (%)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Main function to collect and plot CPU utilization
def main():
    num_samples = 60  # Number of samples to collect
    cpu_data = [[] for _ in range(psutil.cpu_count(logical=True))]  # List to store per-core CPU data
    timestamps = []  # List to store timestamps
    
    for _ in range(num_samples):
        cpu_percentages = get_cpu_utilization()
        timestamps.append(datetime.datetime.now().strftime('%H:%M:%S'))
        
        for core in range(len(cpu_percentages)):
            cpu_data[core].append(cpu_percentages[core])
        
        time.sleep(1)  # Wait for 1 second before collecting next sample
    
    plot_cpu_utilization(cpu_data, timestamps)

if __name__ == "__main__":
    main()
