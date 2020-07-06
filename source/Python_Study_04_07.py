# sort(*, key=None, reverse=False)
list1 = [1, 3, 4, 5, 2, 6]
list2 = ["hello", "python", "world", "program", "is", "good"]
list3 = [1, 3, 6, 4, 2, 5]

# 기본 사용
list1.sort()
print(list1)

# 특정한 값 정렬
# 글자의 길이에 따른 정렬
list2.sort(key=lambda x:len(x))
print(list2)

# 내림차순 정렬
list3.sort(reverse=True)
print(list3)
