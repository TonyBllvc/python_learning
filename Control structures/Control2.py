#List-operations
nums = [7, 7, 7, 7, 7]
nums[2] = 5
print(nums)

#eg
nums = [1, 2, 3, 4, 5]
nums[3] = nums[1]
print(nums[3])

#List-operations 2
nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)

#eg
nums = [33, 42, 56]
nums[1] = 22
print(nums)

#List Operations
words = ["spam", "eggs", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

#eg
nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1] - 5
if 4 in nums:
    print(nums[3])
else:
    print(nums[4])

#List-operations
nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)

#eg
letters = ['a', 'b', 'z']
if "z" in letters:
    print("yes")

#List-Functions
nums = [1, 2, 3]
nums.append(4)
print(nums)

#eg
words = ["Hello"]
words.append("world")
print(words[1])

#List-functions
nums = [1, 3, 5, 2, 4, 5]
print(len(nums))

#eg
letters = ["a", "b", "c", "d"]
letters.append("d")
print(len(letters))

#List-functions
words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words)

#or
words = ["Python", "fun"]
words.insert(1, "is")
print(words)

#Eg
nums = [9, 8, 7, 6, 5]
nums.append(4)
nums.insert(2, 11)
print(len(nums))

#List functions
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))
#print(letters.index('z'))

#eg
list = ['w', 'x', 'y']
list.append('z')
print(len(list))

