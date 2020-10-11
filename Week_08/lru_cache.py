#146. LRU缓存机制

class LRUCache:

    def __init__(self, capacity: int):
        self.data=collections.OrderedDict()
        self.remain=capacity

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1

        #存在指定的key 则获取其v  并删除后重新插入。让最近访问的元素保持在最前面
        v = self.data.pop(key)
        self.data[key]=v
        return v

    def put(self, key: int, value: int) -> None:
        #存在的话要删除原来的位置 把它放在最新的位置
        if key in self.data:
            self.data.pop(key)
            #data[key] = v
        else:
            #不存在key的话 在插入到新的位置前 看最后的元素位置离容量上限还有多少
            #已经达到容量上限 则删除最远的未被使用的元素
            if self.remain ==0:
                self.data.popitem(last=False)
            else:
                #未到容量上限 则离上限的距离-1后 直接插入到前面的位置
                self.remain-=1
        #无论存在与否 最新写入的数据都要放在最前面的的位置
        self.data[key] =value