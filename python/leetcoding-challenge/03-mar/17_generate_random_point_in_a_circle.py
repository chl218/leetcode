"""
Given the radius and x-y positions of the center of a circle, write a function randPoint which generates a uniform
random point in the circle.

Note:

    input and output values are in floating-point.
    radius and x-y position of the center of the circle is passed into the class constructor.
    a point on the circumference of the circle is considered to be in the circle.
    randPoint returns a size 2 array containing x-position and y-position of the random point, in that order.

Example 1:

Input:
["Solution","randPoint","randPoint","randPoint"]
[[1,0,0],[],[],[]]
Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]

Example 2:

Input:
["Solution","randPoint","randPoint","randPoint"]
[[10,5,-7.5],[],[],[]]
Output: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]

Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has three arguments, the
radius, x-position of the center, and y-position of the center of the circle. randPoint has no arguments. Arguments are
always wrapped with a list, even if there aren't any.
"""

import math


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        theta = math.uniform(0, 2*math.pi)
        R = self.r * math.sqrt(math.uniform(0, 1))
        return [self.x + R * math.cos(theta), self.y + R * math.sin(theta)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()

"""
Imagine first special case for this problem: we have circle with radius equal to 1 and coordinates of center is (0, 0).
Let us use polar coordinates:
x = R * cos(theta)
y = R * sin(theta).


Here R is distance between our point (call it A) and the origin (call it O). theta is angle between OA and axis OX.
Why it is good idea to go to polar coordinates here? Because in polar coordiantes unity circle can be written as:
R <= 1
0 <= theta <= 2*pi.

Now we need to answer two qustions: how to generate R and how to generate theta.

    About theta it is quite obvious: we do it uniformly.
    About R it is not obvious: if we do it uniformly, there will be more points closer if we generate it in uniform way.
      Look at this intuition: let us fix R = 1 and generate 10 points, then fix R = 0.5 and generate 10 more points.
      What you can see? Distance between points on the big circle is in average 2 times bigger, than between 2 points
      on smaller circle. It actually means, that for small circle you need to generate only 5 points, not 10, and by
      this logic if you have x points for circle with R = 1, you need x*R points for smaller radius.


This was intuition, now let go into mathematics: what does uniform distribution means, that if we choose small element
inside our circle, than probability to get inside this element should be proportional to area of this element. Let us
define F(R) cumulative distribution function (cdf) for radius. Then by definition probability to get between R and
R + dR is equal to F(R + dR) - F(R) = f(R)*dR, where f(R) is probability density function (pdf), so probability to get
into this small region is f(R)* dR * dTheta. From other point of view, area of this region can be calclated as
[(R+dR)^2 - R^2]*dTheta = 2*R*dR*dTheta. From here we get, that f(R) = c*R for some constant c (because we say it is
proportional, not equal). Now, F'(R) = f(R), so F(R) = c*R^2 (here c is another conatant). Now the question is how you
generate data such that cumulative function is proportional to R^2. The answer is Inverse transform sampling (check
wikipedia), where idea is given uniform distribution generate data from any distribution F(R): we need to generate R
from uniform distrubution and than apply inverse function, that is we have sqrt(uniform(0,1)) in the end.
"""