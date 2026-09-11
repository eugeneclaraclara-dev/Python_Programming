# for문
# for (int i = 0; i < 10; i++)
# for in iterable 객체

for i in range(5):
    print(i, end=" ")
print()

a = range(5)
print(a.start, a.stop, a.step)

# 1 ~ 5

for i in range(1, 6, 1):
    print(i, end=" ")

print()

# 0 ~ 10
for i in range(0, 11, 2):
    print(i, end=" ")

print()

# 5 4 3 2 1 출력
for i in range(5, 0, -1):
    print(i, end=" ")

print()

# 1 ~ 10까지의 합
tot = 0
for i in range(1, 11, 1):
    tot += i
else:
    print(f"sum = {tot}")
print()

print(f"sum = {sum(range(1, 11, 1))}")

s = "hi12한글勪🫰"

for c in s:
    print(c, end=" ")

print()
print(len(s))

# 구구단 출력
# 2 * 1 = 2  2 * 2 = 4 2 * 3 = 6

for i in range(2, 10, 1):
    for j in range(1, 10, 1):
        print(f"{i} * {j} = {i*j:<5d}", end="   ")
    print()
else:
    print("end")
