class TimeMap:

    def __init__(self):
        self.time={} #dic[key]=[[value,timestamp]]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time:
            self.time[key]=[(value,timestamp)]
        else:
            self.time[key].append((value,timestamp))

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time or not self.time[key]:
            return ""
        l=0
        h=len(self.time[key])-1
        res = ""
        while l<=h:
            mid=(l+h)//2
            if self.time[key][mid][1]==timestamp:
                return self.time[key][mid][0]
            elif self.time[key][mid][1]<timestamp:
                res = self.time[key][mid][0]
                l=mid+1
            else:
                h=mid-1
        return res