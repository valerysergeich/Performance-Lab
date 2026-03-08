import sys

def read_ellipse(file_path):
    with open(file_path) as f:
        center = list(map(float, f.readline().split()))
        radius = list(map(float, f.readline().split()))
    return center, radius

def read_points(file_path):
    with open(file_path) as f:
        points = [list(map(float, line.split())) for line in f]
    return points

def check_point(point, center, radius):
    x, y = point
    cx, cy = center
    rx, ry = radius

    value = ((x - cx) ** 2 / rx ** 2) + ((y - cy) ** 2 / ry ** 2) # Уравнение эллипса
    
    if value == 1:
        return 0
    elif value < 1:
        return 1
    else:
        return 2

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py ellipse_file points_file")
        return
        
    ellipse_file = sys.argv[1]
    points_file = sys.argv[2]
    
    center, radii = read_ellipse(ellipse_file)
    points = read_points(points_file)
    
    for point in points:
        result = check_point(point, center, radii)
        print(result)

if __name__ == "__main__":
    main()
