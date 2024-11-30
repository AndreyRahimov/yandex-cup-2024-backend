from itertools import product

n, m = int(input()), int(input())
xs, bs = [int(i) for i in input().split()], [int(i) for i in input().split()]
numbers = []
combinations_number = min(n, 4)

for combination in product(range(23), repeat=combinations_number):
    if all(sum(xs[i] ** j * combination[j] for j in range(combinations_number)) % 23 == bs[i] for i in range(m)):
        numbers = combination
        break

print("".join(chr(number + 97) for number in numbers) + "a" * (n - 4))
