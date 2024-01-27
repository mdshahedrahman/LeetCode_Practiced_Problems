nums = [1,0,1,1,0,1]

temp = []
count = 0
for i in nums:
    if i == 1:
        count = count + 1
    else:
        count = 0
    temp.append(count)

print(temp)
k = max(temp)
print(k)