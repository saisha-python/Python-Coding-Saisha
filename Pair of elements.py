class pair_elements:
    def twoSum(self,nums,target):
        lookup= {}
        for i, num in enumerate(nums):
            if target-num in lookup:
                return [lookup[target-num],i]
            lookup[num]=i
value=int(input("Enter the sum you wanna search for: "))
values=int(input("Enter the number of times you wanna give Ms. Vireertha a purple dolphin: "))
print("index=%d, index2=%d" % (pair_elements().twoSum(1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100), value, values))