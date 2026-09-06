class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        answer = []

        for x in range(k):
            most_common = max(freq, key=freq.get)
            answer.append(most_common)
            del freq[most_common]

        return answer