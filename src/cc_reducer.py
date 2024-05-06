#!/home/bigdata/anaconda3/bin/python
import sys
import json
import numpy as np
from sklearn.mixture import GaussianMixture
import time

def main():
    data_points = []
    start_time = time.time()
    for line in sys.stdin:
        try:
            features = json.loads(line)
            data_points.append(features)
        except json.JSONDecodeError as e:
            sys.stderr.write(f"ERROR: Could not decode JSON from line {line}: {str(e)}\n")
            continue

    if data_points:
        data_array = np.array(data_points)
        gmm = GaussianMixture(n_components=3, max_iter=100)
        gmm.fit(data_array)

        # Print results
        print("Means:", gmm.means_)
        print("Covariances:", gmm.covariances_)

        # Optional: Print execution time
        print("Duration: %s seconds" % (time.time() - start_time))
    else:
        sys.stderr.write("No valid data points received.\n")

if __name__ == "__main__":
    main()
