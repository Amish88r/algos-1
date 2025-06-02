def solve():
    try:
        with open("input2.txt", "r") as infile:
            n = int(infile.readline())
            nums_str = infile.readline().split()
            nums = [int(x) for x in nums_str]
    except FileNotFoundError:
        print("Error: input2.txt not found.")
        return

    tails = []
    for num in nums:
        if not tails or num > tails[-1]:
            tails.append(num)
        else:
            l, r = 0, len(tails) - 1
            while l <= r:
                mid = (l + r) // 2
                if tails[mid] < num:
                    l = mid + 1
                else:
                    r = mid - 1
            if l < len(tails):
                tails[l] = num

    longest_increasing_subsequence = []
    predecessors = {}
    last = -float('inf')
    length = 0
    end_index = -1

    dp = [1] * n
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
        if dp[i] > length:
            length = dp[i]
            end_index = i

    result_sequence = []
    curr = end_index
    while curr != -1:
        result_sequence.append(nums[curr])
        curr = prev[curr]

    result_sequence.reverse()

    try:
        with open("output2.txt", "w") as outfile:
            outfile.write(str(len(result_sequence)) + "\n")
            outfile.write(" ".join(map(str, result_sequence)) + "\n")
    except IOError:
        print("Error: Could not write to output2.txt.")

if __name__ == "__main__":
    solve()