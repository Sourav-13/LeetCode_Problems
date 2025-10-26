# O(n^2) bad
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans_list =[]
        for i in range(len(boxes)):
            min_count = 0
            for j in range(len(boxes)):
                if j !=i and boxes[j] != '0':
                    min_count +=abs(i-j)
            ans_list.append(min_count)
        return ans_list
    
    
# O(n) good
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        
        # Left to right
        balls = 0
        operations = 0
        for i in range(n):
            answer[i] += operations
            if boxes[i] == '1':
                balls += 1
            operations += balls
        
        # Right to left
        balls = 0
        operations = 0
        for i in range(n-1, -1, -1):
            answer[i] += operations
            if boxes[i] == '1':
                balls += 1
            operations += balls
        
        return answer
