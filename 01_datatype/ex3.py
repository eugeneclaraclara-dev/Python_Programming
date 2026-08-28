# 불리언 타입(bool)

a = True  # 참 값을 가진다.
print(a, type(a))

print(2 < 3)  # true
print(2 > 3)  # false
print(2 == 3)  # false
print(2 != 3)  # true

print("apple" > "banana")  # 사전순. a보다 b가 먼저 오니까 false

# bool()
print(bool(3))  # T
print(bool(0))  # F
print(bool("hello"))  # T
print(bool())  # F
print(bool([10]))  # T
print(bool([]))  # F

# None 자료형
a = None  # 아직 값이 정해지지 않아 자료형을 정할 수 없음.
print(type(a))  # NoneType
print(bool(a))  # F
