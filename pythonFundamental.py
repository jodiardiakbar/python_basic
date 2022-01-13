# list comprehension
list1 = [x ** 2 for x in range(10)]
print(f"list1 = {list1}")

list2 = [x ** 2 for x in range(10) if x > 5]
print(f"list2 = {list2}")

# set comprehension
set1 = {x ** 2 for x in range(10)}
print(f"set1 = {set1}")

# dictionary comprehension
dict1 = {x: x ** 2 for x in range(10)}
print(f"dict1 = {dict1}")

# lambda function
add_function = lambda x, y: x + y
print(add_function(5, 3))

# map(function, sequence)
map_result = map(lambda a: a * 10, range(10))
print(f"map_result = {list(map_result)}")

# filter(function, sequence)
filter_result1 = filter(lambda a: a * 10, range(10))
print(f"filter_result1 = {list(filter_result1)}")
filter_result2 = filter(lambda b: b > 5, range(10))
print(f"filter_result2 = {list(filter_result2)}")

# generators
def gen_demo():
    n = 1
    yield n

    n += 1
    yield n

    n += 1
    yield n

test = gen_demo()
print(test)
print(next(test))
print(next(test))
print(next(test))
# print(next(test))

test2 = gen_demo()
for a in test2:
    print(a)

def xor_static_key(a):
    key = 0x5
    for i in a:
        yield chr(ord(i) ^ key)

for z in xor_static_key("test"):
    print(f"xor_static_key = {z}")

xor_static_key2 = (chr(ord(i) ^ 0x5) for i in "test")
print(xor_static_key2)
for m in xor_static_key2:
    print(f"xor_static_key2 = {m}")

# iterators
my_iter = iter(range(4))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

my_iter2 = iter(range(4))
for i in my_iter2:
    print(i)




