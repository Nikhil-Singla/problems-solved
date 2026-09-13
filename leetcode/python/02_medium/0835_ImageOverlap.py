class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        hashmap = defaultdict(int)

        first_ones = []
        second_ones = []

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    first_ones.append((i, j))
                
                if img2[i][j] == 1:
                    second_ones.append((i, j))

        ongoing = 0

        for i1, i2 in first_ones:
            for j1, j2 in second_ones:
                key = str(i1 - j1) + "," + str(i2 - j2)
                hashmap[key] += 1

                if hashmap[key] > ongoing:
                    ongoing = hashmap[key]

        return ongoing
