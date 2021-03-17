"""
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee
representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the
transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Example 2:

Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6



Constraints:

    1 < prices.length <= 5 * 104
    0 < prices[i], fee < 5 * 104

Hint:
   Consider the first K stock prices. At the end, the only legal states are that you don't own a share of stock, or
   that you do. Calculate the most profit you could have under each of these two cases.
"""


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        cash, hold = 0, -prices[0]

        for i in range(len(prices)):
            prevCash = cash
            cash = max(prevCash, hold + prices[i] - fee)
            hold = max(hold, prevCash - prices[i])

        return cash


"""
The following concepts may help:
cash = profit, should always be positive
hold = balance, can be negative or positive.
on i-th day,

    If you do not have a share, your profit is the same as previous day's profit.
    If you hold a share already, you can always get more money when you sell (the prices[i]). But can you earn profit? it depends the balance, so profit = balance + prices[i] - fee when you sell a share on i-th day.
    So on i-th day, max profit = max (profit, balance + prices[i] - fee) (not sell or sell)

now, we need to know how to calculate balance.
on i-th day

    If you already have a share, you cannot buy another share, the balance is the same as previous day's balance.
    If you have no share, so you must have profit (may be 0) and we can use profit to buy a share at cost of prices[i]. After buying a share, balance = profit - prices[i]
    So on i-th day, max balance = max(balance, profit - prices[i]. We need maximize balance since we can get more profit when we sell a share.

Note:

    On a specific day, you either hold a share or not. When you hold a share, we talk about balance. Since you haven't sell you share, we cannot talk about profit.
    When you have no share, you must have profit (cash) since you have sold your share.
    Why we need calculate profit and balance both each day? Because we don't know the status of each day. To get max profit, we need take account of both situation for each day.
    On day one, profit=0 since we have no share to sell. balance = -prices[0] since we need buy a share and we only talk about balance when we have a share.
    In the loop, since we calculate profit based on previous balance, so we need calculate today's profit first, then update the balance of today.
"""