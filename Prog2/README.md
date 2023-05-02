# README for is_interweaving

This Python script checks if a given string `s` can be formed by interweaving two other strings `x` and `y`. The script reads the input from a file and prints the result to the console. The script is divided into two parts: `main.py` and `is_interweaving.py`.

## Dependencies

- Python 3.6 or later

## Files

- `main.py`: The main script that reads input from a file and calls the `is_interweaving` function.
- `source/is_interweaving.py`: Contains the `is_interweaving` function that checks if a string can be formed by interweaving two other strings.
- `dofile`: A sample input file containing strings to check for interweaving.

## Usage

Run the script with the following command:

```
python main.py --input dofile
```

Replace `dofile` with the path to your input file, if necessary.

## Input file format

The input file should contain a single line with three space-separated strings: `s`, `x`, and `y`.

Example:

```
1000 1 00
```

## Output

The script will print the input strings and the result of the `is_interweaving` function. The result is a tuple containing a boolean value and the number of comparisons made during the process. The boolean value is `True` if the given string `s` can be formed by interweaving strings `x` and `y`, otherwise, it is `False`.

Example output:

```
['1000', '1', '00']
(True, 15)
```