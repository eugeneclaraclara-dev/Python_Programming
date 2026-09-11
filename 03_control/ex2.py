# 반복문: while문, for문

# while문
# 1 ~ 10까지 반복 출력
i = 0
while i < 10:
    i += 1
    print(i)
    # if i == 5:
    #     break
else:
    print("End")

nums = [1, 3, 5, 7, 9]
target = 8
i = 0
found = False

while i < len(nums):
    if nums[i] == target:
        print(f"{target} found")
        found = True
        break
    i += 1
# else:
#     print(f"{target} not found")
if found == False:
    print(f"{target} not found")

# 1 ~ 10까지의 합
i = 1
tot = 0
while i <= 10:
    i += 1
    if i % 2 == 1:
        continue
    tot += i

print(f"sum = {tot}")
