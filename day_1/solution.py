import sys

with open(sys.argv[1]) as f:
    input: list[str] = [line.strip() for line in f.readlines()]

calories_per_elf: list[int] = [0]

for line in input:
    if line:
        calories = int(line)
        calories_per_elf[-1] += calories
    else:
        calories_per_elf.append(0)

print(sorted(calories_per_elf, reverse=True)[0])
top_3 = sorted(calories_per_elf, reverse=True)[0:3]
print(sum(top_3))
