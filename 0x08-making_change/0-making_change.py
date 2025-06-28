#!/usr/bin/python3
"""
A module for solving the makeChange problem.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    This function uses an efficient dynamic programming approach to handle large
    totals and pass runtime checks.

    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The total amount to be met.

    Returns:
        int: Fewest coins needed, or -1 if the total cannot be met.
    """
    if total <= 0:
        return 0

    # dp[i] will store the minimum coins required for amount i.
    # Initialize with a value that indicates an amount is unreachable.
    # Using total + 1 as this "infinity" value is a safe choice.
    dp = [total + 1] * (total + 1)

    # Base case: 0 coins are needed to make an amount of 0.
    dp[0] = 0

    # --- OPTIMIZED LOOP STRUCTURE ---
    # Iterate through each coin denomination first.
    for coin in coins:
        # For each coin, update the dp table for all amounts
        # from the coin's value up to the total.
        for amount in range(coin, total + 1):
            # The minimum coins for the current 'amount' is the minimum of:
            # 1. Its current value (from previous coin iterations).
            # 2. 1 + the value for the remaining amount (dp[amount - coin]).
            dp[amount] = min(dp[amount], 1 + dp[amount - coin])

    # If dp[total] was never updated from its "infinity" value,
    # it means the total is not reachable.
    if dp[total] > total:
        return -1
    else:
        return dp[total]
