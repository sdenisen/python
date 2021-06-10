count = int(input())
bit_count = 0
max_count = 0

for _ in range(count):
    bit = input()
    if int(bit) == 0:
        bit_count=0
        continue
    bit_count += 1
    max_count = max(max_count, bit_count)
print(max_count)

