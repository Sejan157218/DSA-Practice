def find_sum(n):
    if n == 1 or n ==0:
        return n
    print("n", n)
    return find_sum(n - 1) + find_sum(n - 2)

print(find_sum(10))