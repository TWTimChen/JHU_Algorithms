import argparse
from source.is_interweaving import is_interweaving


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True, help="file that store the input")
    args = parser.parse_args() 

    buffer = None
    with open(args.input, 'r') as f:
        buffer = f.readline().strip().split(' ')
    print(buffer)
    print(is_interweaving(buffer[0], buffer[1], buffer[2]))


if __name__ == '__main__':
    main()