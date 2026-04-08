class TimeMap:

    def __init__(self):
        self.hash=defaultdict(list)# alice:[("happy",1),("sad",2)]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        l,r=0,len(self.hash[key])-1
        array=self.hash[key]
        value=("",-1)
        while l<=r:
            mid=(l+r)//2
            if array[mid][1]==timestamp:
                return array[mid][0]
            if array[mid][1]<timestamp:
                if value[1]<array[mid][1]:
                    value=array[mid]
                l = mid+1
            else:
                r = mid-1
        return value[0]

        
