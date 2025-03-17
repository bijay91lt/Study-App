import re

def extract_categories(input_file, output_file):
    """
    Extracts category names from an input file and saves them to an output file.

    Args:
        input_file (str): The path to the input file.
        output_file (str): The path to the output file.
    """
    categories = []
    with open(input_file, 'r') as f:
        for line in f:
            match = re.search(r"Category:([A-Za-z0-9_]+)\.txt", line)
            if match:
                categories.append(f"Category:{match.group(1)}")

    with open(output_file, 'w') as f:
        f.write("categories = [\n")
        for category in categories:
            f.write(f'    "{category}",\n')
        f.write("]\n")

# Example usage:
input_file = "datasets/data.txt"  # Replace with your input file path
output_file = "datasets/data1.txt"  # Replace with your desired output file path

extract_categories(input_file, output_file)