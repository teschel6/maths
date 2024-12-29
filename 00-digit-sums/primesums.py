import argparse
import csv
from sum import digit_sum

def is_prime(num):
    """
    Check if a number is prime.
    
    Parameters:
        num (int): The number to check.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(n):
    """
    Generate the first n prime numbers.
    
    Parameters:
        n (int): The number of primes to generate.
    
    Returns:
        list: A list containing the first n primes.
    """
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def main(range_limit=100, output_file=None):
    """
    Calculate the digit sums for first n prime numbers and print the results.
    Optionally, save the results to a CSV file.
    
    Parameters:
        range_limit (int): The upper limit of the range (exclusive).
        output_file (str): Path to the output CSV file (optional).
    """
    results = [(i, digit_sum(i)) for i in generate_primes(range_limit)]

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
    parser = argparse.ArgumentParser(description="Calculate digit sums for prime numbers.")
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
