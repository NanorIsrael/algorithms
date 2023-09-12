myArr = [1,9,2,8,3,7,4, 0, 101]

biggest = myArr[0]
second_biggest = myArr[1]
myArr = sorted(myArr)
for num in myArr:
	if num > biggest:
		second_biggest = biggest
		biggest = num

print(myArr)
print(second_biggest)