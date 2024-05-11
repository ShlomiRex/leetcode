"""
Runtime: 146 ms beats 89%
Memory: 19 MB beats 22%
Time taken: 1 hour 32 minutes, including looking at the solutions.

Very hard question to understand, but the code itself is not difficult.
---------------------------------------------------

Least amount of money needed to form a paid group
Select k workers?

quality = [10,20,5], wage = [70,50,30], k = 2
Selected workers (index): 0, 2
Worker 0 we pay 70 he has quality 10.
Worker 2 we pay 30 he has quality 5.
However, 2nd worker his quality is half of that of worker 0th. Therefor, we either: decrease pay of worker 0, or increase pay of worker 2nd.
We can't decrease pay of worker 0 because by rule 1, every worker must be paid at least heir minimum wage.
So we increase pay of worker 2nd from 30 to 35, since its half wage of worker 0th.
In total we have paid workers: [70, 35] = 105.

quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
Selected workers (index): 0th, 2nd, 3rd.
Worker 0 we pay 4 with quality 3.
Worker 2 we pay 2 with quality 10.
Worker 3 we pay 2 with quality 10.
Because workers 2,3 have quality 10, they must have better proportional salary than worker 0.
Therefor workers 2nd and 3rd will be paid: 4*10/3=13.33333

The highest wage to quality ratio is what determines the wages of other workers.
WE can calculate ratio array and sort it.
We can try be greedy: we pick lowest K workers sorted by lowest ratio. Lower ratio = means higher quality, lower pay (Wage/Quality ratio)
So first example: [(2.5, 50, 20), (6.0, 30, 5), (7.0, 70, 10)] where each tuple is Ratio, Wage, Quality
We pick first 2 workers. The least amount of money we'll pay is:
The 1st worker has ratio of 6, which dominates worker 0th. So we pay 30 (full amount of worker 1).
Then worker 0 will be paid more: 50*(worker1ratio/worker0ratio) = 50*(6/2.5)=120.
But its not the minimum amount of money we can pay. 
If we select worker 1st and 2nd, we have:
Worker 2nd has higher ratio, so we pay him the full amount: 70
Worker 1st has lower ratio, so we need to compensate him, we'll pay him: 30*(7/6)=35
For a total of 105, which is the minimum we can pay.

So:
1) We observe that hiring workers with lower wage/quality ratio leads to lower overall cost of other workers.
2) We calculate the wage per unit of quality, so given ratio and quality we can calculate how much this worker costs: ratio/quality = (wage/quality)/quality = wage
3) The total cost of the hired workers depends on total qualities of the workers so far, and their ratio.
4) Total cost is calculated as the sum of the products of each worker's quality and their wage-to-quality ratio.
5) To manage worker's quality we use max heap: maintain k workers with highest qualities, allowing us to calculate the total cost for the current set of k workers.

The max-heap contains k workers with max qualities. We maintain max-heap of size k by checking lengh of heap:
if greater than k we pop. If its equal to k, we finnaly check the answer: we calculate total cost, and return
the minimum total cost.

We start at sorted workers with smallest ratios. We add to max-heap (that compares quality) so we keep max quality at the root.

"""
from typing import List
import heapq
def mincostToHireWorkers(quality: List[int], wage: List[int], k: int) -> float:
    n = len(quality)
    buckets = [0] * n # Triple tuple: ratio, wage, quality
    for i in range(n):
        buckets[i] = (wage[i] / quality[i], wage[i], quality[i])
    buckets.sort(key=lambda x: x[0])
    
    max_heap = []
    total_qualitiy = 0
    total_cost = float('inf')
    for i in range(n):
        _quality, _ratio = buckets[i][2], buckets[i][0]
        heapq.heappush(max_heap, ( - _quality)) # Max-heap requires minus
        total_qualitiy += _quality

        if len(max_heap) > k:
            total_qualitiy += heapq.heappop(max_heap) # Plus quality since quality in the max-heap is negative

        if len(max_heap) == k:
            total_cost = min(total_cost, total_qualitiy * _ratio)
    
    return total_cost

if __name__ == "__main__":
    assert mincostToHireWorkers(quality = [10,20,5], wage = [70,50,30], k = 2) == 105
    res = mincostToHireWorkers(quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3)
    assert round(res, 5) == 30.66667