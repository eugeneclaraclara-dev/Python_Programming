# 딕셔너리 기초

# ===========================================================
#  딕셔너리 (dict): 키와 값 쌍으로 저장하는 변경 가능한 자료형
#  딕셔너리의 특징
#  1. ( mutable, 변경 가능 )
#  2. ( iterable, 반복 가능 )
#  3. ( sequence X, 인덱싱과 슬라이싱 불가 )
#  4. ( 키는 중복 불가, 값은 중복 가능 )
# ===========================================================

# 딕셔너리 생성
a = {}
b = dict()
print(type(a), type(b))

d = {"id": 1421, "name": "이유진", "age": 17}

# 키로 값 가져오기
print(d["name"])
# print(d["phone"])
print(*d.values())

# 에러가 안나게 하려면?
if "phone" in d:
    print(d["phone"])
print(d.get("phone"))  # None
print(d.get("phone", "전화없음"))
# ===========================================================
# 1. 딕셔너리는 mutable하다. (변경 가능)
# ===========================================================
d["age"] += 1
print(d["age"])

d["phone"] = "6862-8824"
print(d)

del d["phone"]  # 값도 같이 삭제된다.
print(d)

print(d.pop("age"))  # 삭제하면서 그 키의 값을 반환한다. -> 18
print(d)  # age 삭제됨.
# ===========================================================
# 2. 딕셔너리는 iterable하다. (반복 가능)
# ===========================================================

# 딕셔너리 순회
for data in d:
    print(data)  # keys만 출력
    print(data, d[data])  # keys와 values 둘 다 출력

for i, data in enumerate(d):
    print(i, data)

for value in d.values():
    print(value)

for key, value in d.items():
    print(key, value)

print(d)
a = d.items()
d["key"] = 100
print(a)  # 실시간으로 반영이 된다.

# ===========================================================
# 3. 딕셔너리는 sequence 객체가 아니다. (인덱싱, 슬라이싱 불가)
# ===========================================================

d[0] = "python"
print(d[0])  # 바뀌지 않고 추가된다. 0은 인덱스가 아니라 새로운 0이라는 key 값이 생긴다.


# ===========================================================
# 4. 딕셔너리는 키는 중복 불가, 값은 중복 가능하다.
# ===========================================================

d = {"kor": 90, "mat": 85, "eng": 80}

d["kor"] = 100
print(d)

d["sci"] = 80
print(d)

# 키로 가능한 것 : immutable 타입 (숫자형, 불리언, 문자열, 튜플) -> hashable type
# 키로 안되는 것 : mutable 타입 (리스트, 딕셔너리, 집합) -> unhashable type
# 키는 해시 가능(hashable) + 프로그램 실행 동안 hash값이 변하지 않아야 함

d[3.14] = 100
print(d)

# d[[1, 2, 3]] = 10
d[(1, 2)] = 10
print(d)  # 튜블은 들어갈 수 있다.
# imuutable만 들어갈 수 있다. 변경 불가한 거. key는 불변해야 하기 때문이다.
# d[{"key1": 100}] = 10
# print(d)

# 딕셔너리가 저장되는 방식
# 1. 딕셔너리 데이터를 저장하기 위한 해시 테이블을 생성함
# 2. hash(key) 함수를 통해 hash값을 얻음
# 3. hash값을 테이블 크기로 압축하여 버킷 인덱스를 계산하고 해시 테이블에 저장함
# 4. key값으로 조회할 때에도 hash(key)로 hash값을 얻어낸 후(동일 hash값) 해당 인덱스로 가서 조회함

# 만약 key에 mutable 타입을 허용했다면?
# 1. hash(key) 함수로 hash값을 얻어 해시 테이블에 저장함
# 2. key 내용이 변경됨
# 3. 다시 hash(바뀐key)를 하면 새로운 hash값이 나옴
# 4. 새 hash값을 이용하여 버킷 인덱스를 계산하고 해시테이블에 조회를 하면 원래 데이터를 찾을 수 없음

print(hash("HellomyNameIsEugeneLeeNicetOmeEtyOU"))
print(hash((234, 2342)))

# ===========================================================
#  파이썬 내장 함수
# ===========================================================

d = {"kor": 90, "mat": 85, "eng": 80}

print(len(d))
# print(sum(d))
print(sum(d.values()))

print(max(d))  # key에 대한 max
print(min(d))
print(max(d.values()))  # values에 대한 max
print(min(d.values()))

print(sorted(d))  # key에 대한 sorted
print(sorted(d.values()))  # values에 대한 sorted
print(
    dict(sorted(d.items(), reverse=True))
)  # key를 기준으로 sorted, 출력은 둘 다 출력됨


# value 기준으로 정렬
def key(x):
    return x[1]


print(dict(sorted(d.items(), key=key)))
print(dict(sorted(d.items(), key=key, reverse=True)))

# 정렬 기준 설정하기
# lambda: 이름 없는(익명) 한 줄짜리 함수를 만듦
# lambda 매개변수1, 매개변수2, ... : 표현식

print(dict(sorted(d.items(), key=lambda x: x[1])))


# 딕셔너리 합치기
d2 = {"sci": 95, "prog": 100}
# print(d + d2)


# 딕셔너리 반복하기
# print(d * 2)

# 멤버십 연산자
print("kor" in d)
print("art" in d)
print(80 in d.values())
print(100 in d.values())
