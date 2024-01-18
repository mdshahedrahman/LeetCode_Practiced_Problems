nums = [2,5,1,3,4,7]
n = 3

temp = []

for j in range(n):
    for i in range(j, 2*n , n):
        temp.append(nums[i])



print("Final :", temp)

