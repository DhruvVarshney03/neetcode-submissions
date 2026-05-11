class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sorted_s1=sorted(s1)
        # print(sorted_s1)
        # for i in range(0,len(s2)-len(s1)):
        #     sub= s2[i:i+len(s1)]
        #     sorted_sub= sorted(sub)
        #     print(sorted_sub)
        #     if sorted_s1==sorted_sub:
        #         return True

        # return False
       

        if len(s1)>len(s2):
            return False
        freq_s1=[0]*26
        count=[0]*26
        for i in range(len(s1)):
            freq_s1[ord(s1[i])-ord('a')]+=1
            count[ord(s2[i])-ord('a')]+=1
        if count==freq_s1:
            return True

        print(freq_s1)
        left=0
        for right in range(len(s1),len(s2)):
            count[ord(s2[right])-ord('a')]+=1
            count[ord(s2[left])-ord('a')]-=1
            print(count)
            if freq_s1==count:
                return True
            left+=1

        return False

