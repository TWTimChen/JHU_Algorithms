from source.closest_pairs import Point, closest


def main():
    P = [
        Point(x=2, y=3), Point(x=12, y=30),
        Point(x=40, y=50), Point(x=5, y=1),
        Point(x=12, y=10), Point(x=3, y=4)
    ]

    print()
    print('These are the input points:')
    for p in P:
        print(p)
    print()

    print('Enter the number of closest pairs you want to find:')
    m = int(input())
    print()

    results = closest(P, m)
    print(f'This are the closest {m} pairs of points with its distance')
    for res in results:
        print(f'{str(res[0])} | distance: {res[1]}')
    print()

if __name__ == '__main__':
    main()