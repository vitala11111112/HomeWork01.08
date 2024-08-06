from random import*
class Strings():
    def strings(self,strings:list[str], nums:list[int])->list:
        origin = []
        for i in nums:
            origin.append(strings[i])
        return origin
    def strings2(self,list:list[int])->list:
        if len(list) == 0:
            return []
        counter = 0
        even = []
        for i in range(len(list)):
            if list[i] % 2 == 0:
                even.append(list[i])
        for i in range(len(even)):
            for j in range(i, len(even)):
                if even[i] > even[j]:
                    even[i],even[j] = even[j],even[i]
        for i in range(len(list)):
            if list[i] % 2 == 0:
                list[i] = even[0]
                even.pop(0)
                    
        return list

        