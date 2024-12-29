import argparse
import csv

def digit_sum(n):
    """
    Calculate the sum of the digits of a given number.
    
    Parameters:
        n (int): The input number (can be positive or negative).
    
    Returns:
        int: The sum of the digits.
    """
    n = abs(n)  # Ensure the number is positive
    return sum(int(digit) for digit in str(n))

def main(range_limit=100, output_file=None):
    """
    Calculate the digit sums for numbers in the range [0, range_limit) and print the results.
    Optionally, save the results to a CSV file.
    
    Parameters:
        range_limit (int): The upper limit of the range (exclusive).
        output_file (str): Path to the output CSV file (optional).
    """
    results = [(i, digit_sum(i)) for i in range(range_limit)]

    if output_file:
        with open(output_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(results)
        print(f"Results saved to {output_file}")
    else:
        for number, dsum in results:
            print(f"Digit sum of {number} is {dsum}")

# Run the main function
if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Calculate digit sums for a range of numbers.")
    parser.add_argument(
        "-r", "--range", type=int, default=100,
        help="Specify the range limit (default: 100)"
    )
    parser.add_argument(
        "-o", "--output", type=str,
        help="Specify the output CSV file to save results"
    )
    args = parser.parse_args()

    # Call main with the specified arguments
    main(range_limit=args.range, output_file=args.output)
