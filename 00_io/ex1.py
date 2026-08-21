# 입출력

a = input()
print(a, end="\n\n")
print(type(a))
print(a, type(a), sep="\n\t")

a = int(a)
print(type(a))

a = int(input())
print(a, "type:", type(a))

b = float(input())
print(b, "type:", type(b))

# 정수 2개 입력
# 100
# 200

a = int(input())
b = int(input())

print(a, b)

a, b, c = input().split()
print(a, type(a))

# map
# map(함수, List 객체)
a, b, c = map(int, input().split())
print(a, b, c)

# 리스트 변환
a = list(map(int, input().split()))
print(a, type(a))
