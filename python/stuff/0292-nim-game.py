"""
You are playing the following Nim Game with your friend:

    Initially, there is a heap of stones on the table.
    You and your friend will alternate taking turns, and you go first.
    On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
    The one who removes the last stone is the winner.

Given n, the number of stones in the heap, return true if you can win the game
assuming both you and your friend play optimally, otherwise return false.



Example 1:
Input: n = 4
Output: false
Explanation: These are the possible outcomes:
1. You remove 1 stone. Your friend removes 3 stones, including the last stone. Your friend wins.
2. You remove 2 stones. Your friend removes 2 stones, including the last stone. Your friend wins.
3. You remove 3 stones. Your friend removes the last stone. Your friend wins.
In all outcomes, your friend wins.


Example 2:
Input: n = 1
Output: true


Example 3:
Input: n = 2
Output: true



Constraints:
    1 <= n <= 2^31 - 1

"""

class Solution:
    def canWinNim(self, n: int) -> bool:
        if n <= 0:
            return False

        if n == 1 or n == 2 or n == 3:
            return True

        if self.canWinNim(n-1) and self.canWinNim(n-2) and self.canWinNim(n-3):
            return False

        return True

# class Solution:
#     def canWinNim(self, n: int) -> bool:
#         return n % 4 != 0


"""
You can always win a Nim game if the number of stones nnn in the pile is not
divisible by 444.

Reasoning

Let us think of the small cases. It is clear that if there are only one, two,
or three stones in the pile, and it is your turn, you can win the game by
taking all of them. Like the problem description says, if there are exactly
four stones in the pile, you will lose. Because no matter how many you take,
you will leave some stones behind for your opponent to take and win the game.
So in order to win, you have to ensure that you never reach the situation where
there are exactly four stones on the pile on your turn.

Similarly, if there are five, six, or seven stones you can win by taking just
enough to leave four stones for your opponent so that they lose. But if there
are eight stones on the pile, you will inevitably lose, because regardless
whether you pick one, two or three stones from the pile, your opponent can pick
three, two or one stone to ensure that, again, four stones will be left to you
on your turn.

It is obvious that the same pattern repeats itself for n=4,8,12,16,… basically
all multiples of 4.
"""
