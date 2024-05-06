#!/home/bigdata/anaconda3/bin/python
import sys
import json

def main():
    first_line = True
    for line in sys.stdin:
        if first_line:  # Skip the header
            first_line = False
            continue
        parts = line.strip().split(',')
        try:
            # Adjust the indices according to the column positions
            balance = float(parts[1])  # Balance is the second column
            purchases = float(parts[3])  # Purchases is the fourth column
            payments = float(parts[14])  # Payments is the fifteenth column
            # Output the necessary features for clustering
            print(json.dumps([balance, purchases, payments]))
        except ValueError as e:
            # Output errors to stderr for diagnostics
            sys.stderr.write(f"ERROR: Failed processing line {line}: {str(e)}\n")

if __name__ == "__main__":
    main()
