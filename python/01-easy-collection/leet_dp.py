

def climbStairs(n: int) -> int:
    """Climbing Stairs

    You are climbing a stair case. It takes n steps to reach to the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can
    you climb to the top?

    Note: Given n will be a positive integer.
    """

    # Better implementation
    #
    # d = {1: 1, 2: 2}
    #     for i in range(3, n+1, 1):
    #         d[i] = d[i-1] + d[i-2]
    #     return d[n]

    dict = {1: 1}

    def count(i):
        if i <= 1:
            return 1

        c1 = dict[i - 1] if i - 1 in dict else count(i - 1)
        c2 = dict[i - 2] if i - 2 in dict else count(i - 2)

        dict[i] = c1 + c2
        return c1 + c2

    for i in range(1, n + 1):
        count(i)

    return dict[n]
