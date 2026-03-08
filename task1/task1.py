import sys

def generate_path(n, m):
    arr = list(range(1, n + 1))
    path = []
    current = 0
    
    while True:
        path.append(arr[current])
        current = (current + m - 1) % n
        if current == 0:
            break
            
    return path

def main():
    if len(sys.argv) != 5:
        print("Usage: python script.py n1 m1 n2 m2")
        return

    n1, m1 = map(int, sys.argv[1:3])
    n2, m2 = map(int, sys.argv[3:5])

    path1 = generate_path(n1, m1)
    path2 = generate_path(n2, m2)

    result = ''.join(map(str, path1 + path2))
    print(result)

if __name__ == "__main__":
    main()
