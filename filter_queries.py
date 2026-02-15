import csv   # built-in module to read/write csv files

# input file contains: query, url
INPUT_FILE = "india_news.csv"

# output file will contain: category, url
OUTPUT_FILE = "url_indian_news.csv"


def detect_category(query):
    """
    this function decides whether a query belongs to
    sports or politics using substring matching
    """

    # convert to lowercase and remove extra spaces
    # so matching becomes case-insensitive
    query = query.lower().strip()

    # if the word "politic" OR "election" appears anywhere in query
    # then classify as Politics
    # note: "politic" matches both "politic" and "politics"
    if "politic" in query or "election" in query:
        return "Politics"

    # if the word "cricket" OR "sport" appears anywhere in query
    # then classify as Sports
    elif "cricket" in query or "sport" in query:
        return "Sports"

    # if no keywords match, return None (means ignore this row)
    else:
        return None


def main():

    # this will count how many valid rows we saved
    saved_count = 0

    # open input file for reading
    # open output file for writing
    # the backslash allows writing this in two lines
    with open(INPUT_FILE, "r", encoding="utf-8") as infile, \
         open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as outfile:

        # read each row as a dictionary:
        # {"query": "...", "url": "..."}
        reader = csv.DictReader(infile)

        # create writer for output file
        # we define which columns we want
        writer = csv.DictWriter(outfile, fieldnames=["category", "url"])

        # write header row: category,url
        writer.writeheader()

        # loop over each row in input csv
        for row in reader:

            # safely get query (if missing, return empty string)
            query = row.get("query", "")

            # safely get url and remove extra spaces
            url = row.get("url", "").strip()

            # if url is empty, skip this row
            if not url:
                continue   # go to next iteration

            # determine category using substring logic
            category = detect_category(query)

            # if category is not None (means it matched)
            if category:

                # write new row into output file
                writer.writerow({
                    "category": category,
                    "url": url
                })

                # increase counter
                saved_count += 1

    # after loop ends, print how many we saved
    print("Saved", saved_count, "articles.")


# this ensures main() runs only when file is executed directly
# not when imported in another file
if __name__ == "__main__":
    main()
