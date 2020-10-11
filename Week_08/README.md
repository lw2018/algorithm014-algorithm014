
#选择排序
```
def selectSort(L):
    length = len(L)
    for i in range(length-1):
        minIndex = i
        index从i+1到最后面 不断比较得出一个最小的放在结果中
        for j in range(i+1,length):
            if L[j]< L[minIndex]:
                minIndex = j
            L[i],L[minIndex] = L[minIndex],L[i]
    return L
```

#插入排序
```
def insertSort(L):
    length = len(L)
    首次进来 第一个元素作为已排序的序列
    for i in range(length-1):
        从已排序号的序列的最后一个位置开始。不断比较它与后一个位置的大小。把i+1位置的值放在已排序序列的争取位置
        for j in range(i,-1,-1):
            if L[j]>L[j+1]:
                L[j],L[j+1]=L[j+1],L[j]
    return L
```
#冒泡排序
```
class Mysort:
    def __init__(self,start,end,count):
        stat end为随机数生成范围
        self.start=start
        self.end=end
        self.count=count

    用冒泡实现排序
    def __mysort__(self):
        生成一个随机数列表
        L_random=random.sample(range(self.start,self.end),self.count)
        L_len=len(L_random)
        对列表进行排序
        for i in range(L_len):
            for j in range(L_len-i-1):
                if L_random[j]>L_random[j+1]:
                    L_random[j],L_random[j+1] =L_random[j+1],L_random[j]
        return L_random
```
