my_friends = ['John', 'Mary', 'Tom']
print(my_friends, type(my_friends))
my_friends[1] = 'Bob'
print(my_friends)

nums = [[1,2,3], [4,5,6]]
print(len(nums))
print(nums[0][2])
nums.append([7,8,9])
print(nums[2][1])
nums.insert(2, [10,11,12])
print(nums)

numbers = [1,2,3,4,5,6,7,8,9,10]
numbers.pop()
numbers.pop(3)
print(numbers)
numbers.remove(6)
print(numbers)

num_list = [11,33,55,22,44]
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)
num_list.sort()
print(num_list)
num_list.sort(reverse=True)
print(num_list)

print(22 in num_list)

name_list = ['My', 'name', 'is', 'Taro']
print(' '.join(name_list))
print('-'.join(name_list))
sushi = 'I like sushi'.split(' ')
print(sushi)