#!/usr/bin/python3
"""
Module for the makeChange function.
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total.

    This function uses a dynamic programming approach to ensure correctness
    and efficiency.

    Args:
        coins (list): A list of the values of the coins in your possession.
                      The value of a coin will always be an integer > 0.
        total (int): The total amount to be met.

    Returns:
        int: The fewest number of coins needed to meet total.
             Returns 0 if total is 0 or less.
             Returns -1 if total cannot be met by any number of coins you have.
    """
    if total <= 0:
        return 0

    # Create a list to store the minimum coins for each amount from 0 to total.
    # Initialize all values to an unreachable number (e.g., total + 1).
    # This value acts as our "infinity" for the sake of comparison.
    dp = [total + 1] * (total + 1)

    # The base case: it takes 0 coins to make an amount of 0.
    dp[0] = 0

    # Build the dp table from the bottom up.
    # Iterate through each amount from 1 up to the total.
    for amount in range(1, total + 1):
        # For each amount, check each coin denomination.
        for coin in coins:
            # If the coin's value is less than or equal to the current amount,
            # it's a candidate for making change.
            if coin <= amount:
                # The number of coins for the current 'amount' can potentially be
                # updated. We take the minimum of its current value and the
                # value of (1 + the pre-calculated coins for the remaining amount).
                # `dp[amount - coin]` gives the minimum coins for the remainder.
                dp[amount] = min(dp[amount], 1 + dp[amount - coin])

    # After filling the table, the answer is in the last cell.
    result = dp[total]

    # If the result is still our "infinity" value, it means the total
    # could not be formed by any combination of the coins.
    if result > total:
        return -1
    else:
        return result
