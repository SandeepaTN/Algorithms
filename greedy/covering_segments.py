from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments.sort(key=lambda x: x.end) 
    while len(segments)>0:
        s=segments[0]
        
        points.append(s.end)
        segments=[i for i in segments if i.start>s.end] 
        
    
    return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
   
    points = optimal_points(segments)

    print(len(points))
    print(*points)
