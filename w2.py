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
    a=[]
    b=[]
    for i in nums:
        if i>=0:
            a.append(i)
        elif i<0:
            b.append(i)
    if len(a)==0:
        num1=min(b)
        a.remove(num1)
        num2=min(b)
        print(num1*num2)
    elif len(a)==1:
            num10=min(b)
            a.remove(num1)
            num20=min(b)
            print(num10*num20)
    elif len(a)==3:
        c=max(a)
        a.remove(c)
        d=max(a)
        print(c*d)
    elif len(a)==4:
        num_1=max(a)
        a.remove(num_1)
        num_2=max(a)
        print(num_1*num_2)
    else:
        ee=max(a)
        a.remove(ee)
        rr=max(a)
        a.remove(rr)
        j=ee*rr
        k=b[0]*b[1]
        if j>k:
            print(j)
        else:
            print(k)
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

