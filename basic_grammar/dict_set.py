# 사전자료형
data = dict()
data["사과"] = "apple"
data["바나나"] = "banana"

print(data)

if "사과" in data:
  print("있어요~")

# 메소드
data = dict()
data["사과"] = "apple"
data["바나나"] = "banana"

key_list = data.keys()
print(key_list)
value_list = data.values()
print(value_list)

# 리스트로 반환할때는
key_list = list(data.keys())
print(key_list)

for key in key_list:
  print(data[key])

# 집합 자료형
data = set([1,1,2,3,4,5,5])
print(data)

data = {1,1,2,3,4,5,5}
print(data)

# 집합 자료형의 연산
a = {1,2,3,4}
b = {2,3,4,5}

print(a|b)
print(a&b)
print(a-b)

# 메소드
data = set([1,2,3])
print(data)

data.add(7)
print(data)

data.update([5,6])
print(data)

data.remove(5)
print(data)