class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        
        sequence_list=[]
        seq_length=1
        num_length=len(nums)
        nums.sort()
        print(nums)
        i=0
        while i<num_length-1:

            if nums[i]==nums[i+1]:
                i+=1
            elif nums[i]==nums[i+1]-1:
                seq_length+=1
                i+=1
            else:
                sequence_list.append(seq_length)
                seq_length=1
                i+=1
        sequence_list.append(seq_length)      
        print(sequence_list)
        return max(sequence_list)