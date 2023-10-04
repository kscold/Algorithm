class Solution(object):
    def generate(self, numRows):
        def generate_row(row_num):
            if row_num == 0:
                return [1]
            if row_num == 1:
                return [1, 1]

            memo = {}

            if row_num in memo:
                return memo[row_num]

            prev_row = generate_row(row_num - 1)

            current_row = [1]
            for i in range(1, row_num):
                current_row.append(prev_row[i - 1] + prev_row[i])

            current_row.append(1)

            memo[row_num] = current_row

            return current_row

        result = []
        for i in range(numRows):
            result.append(generate_row(i))

        return result

numrows = int(input())
solution = Solution()
pascal = solution.generate(numrows)
print(pascal)