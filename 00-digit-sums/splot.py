import matplotlib.pyplot as plt
import csv
import argparse

def read_csv(file_path):
    """
    Reads a CSV file and extracts a sequence of numbers.
    
    Parameters:
        file_path (str): Path to the CSV file.
    
    Returns:
        tuple: A tuple containing indices and sequence.
    """
    indices = []
    sequence = []
    
    with open(file_path, mode='r') as csvfile:
        reader = csv.reader(csvfile)
        for index, row in enumerate(reader):
            if len(row) > 0:
                indices.append(index)  
                sequence.append(int(row[1])) 

    return indices, sequence

def plot_sequence(indices, sequence):
    """
    Plots a sequence based on provided x-values and sequence data.
    
    Parameters:
        indices (list): The x-values for plotting.
        sequence (list): The sequence of values to be plotted.
    """
    plt.plot(indices, sequence)

    # Add labels and title
    plt.title("Plot of Sequence from CSV")
    plt.xlabel("X-Values")
    plt.ylabel("Sequence Value")

    # Show the plot
    plt.show()

if __name__ == "__main__":
    
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Plot a sequence from a CSV file.")
    parser.add_argument(
        "input", type=str,
        help="Path to the input CSV file containing the sequence."
    )
    args = parser.parse_args()

    print("Plotting Sequence from:", args.input)

    # Read the CSV file and get indices and sequence
    indices, sequence = read_csv(args.input)

    

    # Plot the sequence
    plot_sequence(indices, sequence)
