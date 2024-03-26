import heapq
from collections import Counter
from typing import List
from heapq import heappush, heappop

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hands = Counter(hand)

        # 카드 빈도수 계산
        card_counts = Counter(hand)
        # 최소 힙 생성
        min_heap = list(card_counts.items())
        heapq.heapify(min_heap)

        while min_heap:
            start_number = min_heap[0][0]
            # looping the iteration starting from the current number to
            #   end of the size of groupSize
            for i in range(start_number,start_number+groupSize):
                # (1) if the number is not cosecutive:
                if i not in card_counts:
                    return False
                # decreasing value of its key
                card_counts[i] -=1

                # (2) if the poped nubmer from the heap
                # is not matched with the expectation
                if card_counts[i]==0:
                    # if min_heap이 [(1, 3), (2, 2), (3, 1)],
                    # heapq.heappop(min_heap) would be (1, 3)
                    # therefore, heapq.heappop(min_heap)[0] == 1
                    if i != heapq.heappop(min_heap)[0]:
                        return False
                    elif card_counts[i] < 0:
                        return False

        return True