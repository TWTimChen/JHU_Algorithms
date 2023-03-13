import random
import time
import csv
from typing import List
from source.closest_pairs import Point, closest


def gen_point(range_x: int, range_y: int) -> Point:
    return Point(
        x = random.randint(0, range_x),
        y = random.randint(0, range_y)
    )

def gen_point_list(
    range_x: int, range_y: int, length: int
) -> List[Point]:
    return [
        gen_point(range_x, range_y) for _ in range(length)
    ]

def main():
    buf = []
    RANGE_X = 1e4
    RANGE_Y = 1e4
    for n in range(50, 250, 50):
        points = gen_point_list(RANGE_X, RANGE_Y, n)
        for m in range(10, int(n*(n-1)/2), 500):
            start_time = time.time()
            closest(points, m)
            end_time = time.time()
            buf.append([n, m, end_time - start_time])
        print(f'Finish n: {n}')

    with open('./test/test_result.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(buf)

if __name__ == '__main__':
    main()
