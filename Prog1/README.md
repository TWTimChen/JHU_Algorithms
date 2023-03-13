# Program Assigment - 1

This program is a Python implementation of an algorithm to find the m closest pairs of points in a set of n points in a two-dimensional plane. The algorithm uses a divide-and-conquer approach that runs in `O(n log n)` time.

To run the program, you will need Python 3 installed on your computer. You can install the required dependencies by running the following command in the terminal:

```
python -m vern .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Once you have installed the dependencies, you can run the program by executing the following command:

```
python closest_pairs.py
```

The program defines a set of points P, and the number of closest pairs to be found, m, is specified as an argument when instantiating the ClosestPairs class. The closest() method of the ClosestPairs class returns a list of the m closest pairs of points, including their x and y coordinates.

For more information about how to use the program, please refer to the comments in the source code.
