from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional
from depq import DEPQ as deque


@dataclass
class Point:
    x: float
    y: float

    def compare_x(self, p: Point) -> float:
        return (self.x - p.x)

    def compare_y(self, p: Point) -> float:
        return (self.y - p.y)

    def dist(self, p: Point):
        return (self.compare_x(p)**2 + self.compare_y(p)**2)**(1/2)

def merge_deq(deq_1, deq_2):
    assert deq_1.size() == deq_2.size()
    n = deq_1.size()
    deq_merge = deque()
    for _ in range(n):
        if deq_1.low() < deq_2.low():
            pop = deq_1.poplast()
        else:
            pop = deq_2.poplast()
        deq_merge.insert(pop[0], pop[1])
    return deq_merge

def brute_force(points: List[Point], n: int, m: int) -> float:
    dummy_dist = float("inf")
    dummy_point = Point(-1, -1)
    deq = deque()
    deq.insert((dummy_point, dummy_point), dummy_dist)
    for i in range(n-1):
        for j in range(i+1, n):
            curr_dist = points[i].dist(points[j])
            if deq.size() < m:
                deq.insert((points[i], points[j]), curr_dist)
                continue
            if curr_dist < deq.high():
                deq.popfirst()
                deq.insert((points[i], points[j]), curr_dist)
    while (deq.size() < m):
        deq.insert((dummy_point, dummy_point), dummy_dist)
    assert deq.size() == m
    return deq

def strip_scan(strip: List[Point], size: int, deq) -> float:
    strip = sorted(strip, key=lambda point: point.y)
    for i in range(size):
        for j in range(i+1, min(i+7, size)):
            curr_dist = strip[i].dist(strip[j])
            if curr_dist < deq.high():
                deq.popfirst()
                deq.insert((strip[i], strip[j]), curr_dist)
    return deq

def closest_recursive(points: List[Point], n: int, m: int) -> float:
    if (n*(n-1)/2 <= m) or (n <= 3):
        return brute_force(points, n, m) 
    mid = n//2
    mid_point = points[mid]
    deq_l = closest_recursive(points, mid, m)
    deq_r = closest_recursive(points[mid:], n - mid, m)
    deq_m = merge_deq(deq_l, deq_r)
    strip = []
    deq_m_max = deq_m.high()
    for i in range(n):
        if abs(points[i].x - mid_point.x) < deq_m_max:
            strip.append(points[i])
    return strip_scan(strip, len(strip), deq_m)

def closest(points: List[Point], m: int) -> float:
    n = len(points)
    assert n*(n-1)/2 >= m
    points = sorted(points, key=lambda point: point.x)
    return closest_recursive(points, n, m)
