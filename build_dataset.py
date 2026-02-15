import csv
import sys

# ------------------------------------------------------------------
# Some news articles can be very long.
# Python's csv module has a maximum field size limit.
# If a text column exceeds that limit, it throws an error.
# This loop safely increases the maximum allowed field size.
# ------------------------------------------------------------------

max_size = sys.maxsize  # start with largest possible integer

while True:
    try:
        csv.field_size_limit(max_size)  # attempt to set max field size
        break  # if successful, exit loop
    except OverflowError:
        # if too large for system, reduce size and try again
        max_size //= 10


# List of input files that will be merged

INPUT_FILES = [
    "indian_news_with_text.csv",
    "bbc-text.csv"
]

# name of final merged dataset
OUTPUT_FILE = "sports_politics_dataset.csv"

# Function to standardize category labels
# Example:
# "sports" → "Sports"
# " POLITICS " → "Politics"
# This ensures consistent labels across datasets.

def normalize_category(label):
    return label.strip().capitalize()

# Function to check whether a row is valid
# Conditions:
# 1. Must have category
# 2. Must have text
# 3. Category must be Sports or Politics

def is_valid_row(row):
    category = row.get("category")
    text = row.get("text")

    # reject row if missing required fields
    if not category or not text:
        return False

    #normalise category before checking
    category = normalize_category(category)

    #keep only desired classes
    return category in {"Sports", "Politics"}


# Main function to:
#   - Read multiple CSV files
#   - Filter valid rows
#   - Write merged dataset
#   - Track statistics

def main():

    total_count = 0              # total valid rows across all files
    per_file_count = {}          # dictionary to store per-file counts

    #open output file once (write mode)
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as outfile:

        #create CSV writer with fixed column names
        writer = csv.DictWriter(outfile, fieldnames=["category", "text"])
        writer.writeheader()  # write column headers

        for file in INPUT_FILES: # process each input file one by one

            file_count = 0  # counter for this file

            #Open input file for reading
            with open(file, "r", encoding="utf-8") as infile:
                reader = csv.DictReader(infile)  # read rows as dictionaries

                for row in reader:
                    # check if row satisfies filtering conditions
                    if is_valid_row(row):
                        # write cleaned row directly to output file
                        writer.writerow({
                            "category": normalize_category(row["category"]),
                            "text": row["text"].strip()  # remove extra spaces
                        })

                        # Update counters
                        file_count += 1
                        total_count += 1

            # Store count for this file
            per_file_count[file] = file_count

    
    # print summary statistics after merging

    print("Dataset built successfully.")
    print("Total samples:", total_count)

    print("Breakdown by file:")
    for file, count in per_file_count.items():
        print(f"  {file}: {count}")


# Run only if script is executed directly (not imported)
if __name__ == "__main__":
    main()