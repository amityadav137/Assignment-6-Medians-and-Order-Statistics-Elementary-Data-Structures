from deterministic_selection import median_of_medians
from randomized_quickselect import quickselect
import random

def run_tests():
    arrays = {
        "random_10": [3, 7, 2, 1, 6, 9, 4, 8, 5, 0],
        "duplicates": [5, 1, 5, 3, 5, 2, 5],
        "sorted": list(range(10)),
        "reverse": list(range(9, -1, -1)),
        "random_100": [random.randint(1, 1000) for _ in range(100)]
    }
    k_values = [0, 3, 5, 9]

    for name, arr in arrays.items():
        for k in k_values:
            if k < len(arr):
                print(f"{name} | k={k} | MoM: {median_of_medians(arr[:], k)} | QS: {quickselect(arr[:], k)}")

if __name__ == "__main__":
    run_tests()