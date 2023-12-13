# 함수
def add(a, b):
  return a+b

print(add(1,2))

def minus(a,b):
  print(a-b)

minus(1,2)

minus(b=5,a=3)

# global
a = 0;
def func():
  global a
  a +=1
  print(a)

func()

array = [1,2,3]
def func2():
  array = [4,5,6]
  array.append(7)
  print(array)

func2()
print(array)

# 여러개의 반환값
def operator(a, b):
  return a+b, a-b, a*b, a/b

x,y,z,w = operator(3,2)
print(x,y,z,w)

# 람다표현식
def adder(a,b):
  return a+b

print(adder(1,2))

print((lambda a,b:a+b)(1,2))


array = [('김', 86), ('이', 72), ('신', 46)]
def my_key(x):
  return x[1]

print(sorted(array, key = my_key))
print(sorted(array, key = lambda x:x[1]))


list1 = [1,2,3]
list2 = [4,5,6]

result = map(lambda a,b:a+b, list1, list2)
print(list(result))