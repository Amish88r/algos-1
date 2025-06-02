def is_valid_sequence(sequence):
    stack = []
    for char in sequence:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

def solve():
    try:
        with open("input2.txt", "r") as infile, open("output2.txt", "w") as outfile:
            N = int(infile.readline())
            for _ in range(N):
                sequence = infile.readline().strip()
                if is_valid_sequence(sequence):
                    outfile.write("YES\n")
                else:
                    outfile.write("NO\n")
    except FileNotFoundError:
        print("Error: input.txt not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    solve()