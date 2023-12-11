import random
import math


class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        angle = random.uniform(0, 2 * math.pi)  # 0부터 2pi 까지 범위에서 랜덤으로 뽑음
        r = math.sqrt(random.uniform(0,
                                     1)) * self.radius  # 0 부터 1까지 범위에서 랜덤으로 뽑은거의 제곱근을 씌워서 랜덤한 제곱근을 얻고 이를 입력받은 반지름이람 곱해서 랜덤한 반지름을 만듬
        x = self.x_center + r * math.cos(angle)  # x축 중심 좌표와 랜덤한 x좌표를 더함
        y = self.y_center + r * math.sin(angle)  # y축 중심 좌표와 랜덤한 y좌표를 더함
        return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()

solution = Solution(1.0, 0.0, 0.0)
print(solution.randPoint())
print(solution.randPoint())
print(solution.randPoint())
