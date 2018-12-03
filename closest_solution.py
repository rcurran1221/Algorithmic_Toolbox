#Uses python3
import sys
import math
from operator import itemgetter

def minimum_distance(x, y):    
    points = get_points_sorted(x, y)
    return minimum_distance_inner(points)
    
def minimum_distance_inner(points):
    if (len(points) <= 3):
        return find_min(points)
    
    first_half, second_half, mid_point = split_points(points)
    
    min_distance_first = minimum_distance_inner(first_half)
    
    min_distance_second = minimum_distance_inner(second_half)
    
    min_distance = min(min_distance_first, min_distance_second)
    
    result_points = filter_by_dist_to_mid(points, mid_point, min_distance)
    
    points_sorted_y = sort_by_y(result_points)
    
    cross_set_min = find_min_cross_set(points_sorted_y, min_distance)
    
    min_distance = min(min_distance, cross_set_min)
    
    return round(min_distance, 4)

def find_min_cross_set(points, min_distance):
    minimum = sys.maxsize
    
    for i in range(len(points)):
        for j in range(i + 1, min(i + 8, len(points))):
            if abs(points[i][1] - points[j][1]) <= min_distance:
                dist = calculate_distance(points[i], points[j])
                minimum = min(minimum, dist)
    
    return minimum

def sort_by_y(points):
    return sorted(points, key = itemgetter(1))

def filter_by_dist_to_mid(points, mid_point, min_distance):
    result_points = []
    
    for i in range(len(points)):
        if abs(points[i][0] - mid_point[0]) <= min_distance:
            result_points.append(points[i])
            
    return result_points
            
def get_points_sorted(x, y):
    points = []
    for i in range(len(x)):
        points.append((x[i], y[i]))
        
    return sorted(points, key = itemgetter(0))

def split_points(points):
    n = len(points)
    mid = n // 2
    return points[:mid], points[mid:], points[mid]

def find_min(points):
    n = len(points)
    minimum = sys.maxsize
    
    for i in range(n):
        for x in range(i + 1, n):
            dist = calculate_distance(points[i], points[x])
            minimum = min(minimum, dist)
    
    return minimum

def calculate_distance(firstPoint, secondPoint):
    xDiff = firstPoint[0] - secondPoint[0]
    yDiff = firstPoint[1] - secondPoint[1]
    squaredSumDiff = (xDiff**2) + (yDiff**2)
    return math.sqrt(squaredSumDiff)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
#    data = list(map(int, input().split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
