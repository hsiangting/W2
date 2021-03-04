#要求一
def calculate(min,max):
    sum=0
    for i in range(min,max+1):
        sum+=i
    print(sum)
calculate(1,3)
calculate(4,8)
#要求二
def avg(data):
    sum=0
    for n in range(0,int(data["count"])):
        n=data["employees"][n]["salary"]
        sum+=n
    print(sum/int(data["count"]))
avg({"count":3,"employees":[{"name":"John","salary":30000},{"name":"Bob","salary":60000},{"name":"Jenny","salary":50000}]})
#要求三
def maxProduct(nums):
    pos=[]
    neg=[]
    for i in nums:
        if i>=0:
            pos.append(i)
        elif i<0:
            neg.append(i)
    if len(pos)<=1:
        min_neg=min(neg)
        neg.remove(min_neg)
        sec_min_neg=min(neg)
        result=min_neg*sec_min_neg
    elif len(neg)<=1:
        max_pos=max(pos)
        pos.remove(max_pos)
        sec_max_pos=max(pos)
        result=max_pos*sec_max_pos
    else:
        min_neg=min(neg)
        neg.remove(min_neg)
        sec_min_neg=min(neg)
        result_neg=min_neg*sec_min_neg
        max_pos=max(pos)
        pos.remove(max_pos)
        sec_max_pos=max(pos)
        result_pos=max_pos*sec_max_pos
        if result_neg>=result_pos:
            result=result_neg
        else:
            result=result_pos
    print(result)    
maxProduct([5,20,2,6])
maxProduct([10,-20,0,3])
#要求四
def twoSum(nums,target):
    for i in range(0,len(nums)):
        for j in range(i,len(nums)):
            if nums[i]+nums[j]==target:
                return([i,j])
result=twoSum([2,11,7,15],9)
print(result)
#要求五
def maxZeros(nums):
    max_time=0
    cur_time=0
    for i in nums:
        if i==0:
            cur_time+=1
            max_time=max((cur_time,max_time))
        else:
            cur_time=0
    print(max_time)
maxZeros([0,1,0,0])
maxZeros([1,0,0,0,0,1,0,1,0,0])
maxZeros([1,1,1,1,1])
