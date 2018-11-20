# Uses python3

from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments, resultPoints):
    
    while len(segments) > 0:
        
        min_endPoint = find_min_endPoint(segments)
        
        resultPoints.append(min_endPoint)
        
        containingSegments = find_segments_by_point(segments, min_endPoint)
        
        remove_segments(segments, containingSegments)
        
        return optimal_points(segments, resultPoints)
    
    return resultPoints

def find_min_endPoint(segments):
    endPoints = []
    
    for s in segments:
        endPoints.append(s.end)
    
    endPoints.sort()
    
    return endPoints[0]

def find_segments_by_point(segments, point):
    containingSegments = []
    
    for s in segments:
        if s.start <= point <= s.end:
            containingSegments.append(s)
            
            
    return containingSegments 

def remove_segments(segments, segmentsToRemove):
    for s in segmentsToRemove:
        segments.remove(s)

if __name__ == '__main__':
    n, *data = map(int, input().split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    resultPoints = []
    points = optimal_points(segments, resultPoints)
    print(len(points))
    for p in points:
        print(p, end=' ')
