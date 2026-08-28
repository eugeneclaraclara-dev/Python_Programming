# 문자열 (str)
# "", ''

a = "python"  # 홑따옴표도 되긴 한다.
print(a, type(a))

print("I'll be back")
print("I'll be back")

# 여러줄 문자열 (not 주석)
a = """
Life is short
You need python
"""
print(a)


# docstring
def func():
    """
    func() 함수에 대한 설명 작성
    이 함수는 어떤 기능을 하고
    입출력값은 이거고 어떻게 만들었다.
    """
    # 첫 번째에 기입하기
    pass


print(func.__doc__)

# 문자열 연결
print("Hello " + "Python")  # 사이에 스페이스 없음.

# 문자열 반복
print("hello " * 10)
print("*" * 30)
# print("Hello" + 3) 문자열은 문자열끼리 더하기. 문자열 연산 시 주의.
print("Hello " + str(3))
print("10" + " 2")
print(int(10) + int(2))

# 문자열 포맷팅 (f-string)
name = "Pororo"
age = 23

print(f"이름: {name}, 나이: {age}세")
print(f"내년 나이: {age + 1}세")
print(f"{name.upper()}")

pi = 3.141592653589793238
print(f"{pi:.3f}")
print(f"{pi:.0f}")

num = 123456789
print(f"{num:,}")

print(f"{num:015,d}")  # 오른쪽 정렬
print(f"{num:<015,d}")  # 왼쪽 정렬
