from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sum = 0
        record = []
        size = len(operations)
        for i in range(size):
            match operations[i]:
                case '+':
                    record.append(record[-1] + record[-2])
                case 'D':
                    record.append(2 * record[-1])
                case 'C':
                    record.pop()
                case _: # This is the default case 
                    val = int(operations[i])
                    record.append(val)

        for i in range(len(record)):
            sum += record[i]

        return sum