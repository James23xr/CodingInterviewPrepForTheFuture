class Solution:
    def binaryGap(self, n: int) -> int:
        binary_representation = bin(n)[2:]
        last_position = -1
        max_distance = 0
        for i, bit in enumerate(binary_representation):
            if bit == '1':
                if last_position != -1:
                    max_distance = max(max_distance,i-last_position)
                last_position = i
        return max_distance
        