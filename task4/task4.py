import sys

def read_numbers_from_file(file_path):
    with open(file_path, 'r') as f:
        numbers = [int(line.strip()) for line in f if line.strip()]
    return numbers

def calculate_moves(nums, target):
    return sum(abs(num - target) for num in nums)

def find_min_moves(nums, max_moves=20):
    nums_sorted = sorted(nums)
    n = len(nums_sorted)

    median = [nums_sorted[n//2]]
    if n % 2 == 0:
        median.append(nums_sorted[n//2 - 1])
    
    min_moves = float('inf')
    
    for med in median:
        for offset in range(-max_moves, max_moves + 1):
            target = med + offset
            moves = calculate_moves(nums, target)
            if moves <= max_moves and moves < min_moves:
                min_moves = moves
    
    if min_moves <= max_moves:
        return min_moves
    else:
        return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_with_numbers>")
        return
    
    file_path = sys.argv[1]
    nums = read_numbers_from_file(file_path)
    
    result = find_min_moves(nums)
    
    if result is not None:
        print(f"Минимальное количество ходов: {result}")
    else:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу")

if __name__ == "__main__":
    main()
