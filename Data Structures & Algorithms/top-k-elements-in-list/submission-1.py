class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums).most_common(k)
        lst=list()
        for freq in freqs:
            lst.append(freq[0])
        return lst