"""
Runtime: 47 ms beats 97%
Memory: 16.7 MB beats 34%

Looked at solutions.
"""
from typing import List
from collections import defaultdict
import heapq
def topKFrequent(words: List[str], k: int) -> List[str]:
    counter = defaultdict(int)
    for word in words:
        counter[word] += 1

    # Create max-heap, notice counter is negative
    # That means the root element will be the most frequent element
    heap = [(-count, word) for word, count in counter.items()]
    heapq.heapify(heap)
    
    return [heapq.heappop(heap)[1] for _ in range(k)]

if __name__ == "__main__":
    assert topKFrequent(["i","love","leetcode","i","love","coding"], 2) == ["i","love"]
    assert topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4) == ["the","is","sunny","day"]