#!/usr/bin/python3
"""
This module contains the solution for the Prime Game interview question.
"""


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game after x rounds.

    Args:
        x (int): The number of rounds to be played.
        nums (list): A list of integers where each integer n represents
                     the upper bound of the set for that round.

    Returns:
        str: The name of the player with the most wins ("Maria" or "Ben").
        None: If the winner cannot be determined (e.g., a tie).
    """
    # --- Step 1: Handle Edge Cases ---
    # If there are no rounds or no numbers, there's no game.
    if x < 1 or not nums:
        return None

    # --- Step 2: Pre-calculate Primes with Sieve of Eratosthenes ---
    # Find the maximum n we will need to consider.
    max_n = max(nums)

    # Create a boolean list to mark numbers as prime or not.
    # is_prime[i] will be True if i is prime, otherwise False.
    # We initialize all numbers as potentially prime.
    is_prime = [True] * (max_n + 1)
    
    # 0 and 1 are not prime numbers.
    is_prime[0] = is_prime[1] = False

    # The Sieve algorithm:
    # We iterate from 2 up to the square root of max_n.
    for i in range(2, int(max_n**0.5) + 1):
        # If a number `i` is still marked as prime...
        if is_prime[i]:
            # ...then all of its multiples are not prime.
            # We can start marking from i*i.
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False

    # --- Step 3: Count Primes and Play the Game ---
    maria_wins = 0
    ben_wins = 0

    # Play each round of the game for each n in the nums list.
    for n in nums:
        # Count the number of primes from 1 up to n.
        # We can do this by looking at our pre-calculated is_prime list.
        prime_count = 0
        for i in range(2, n + 1):
            if is_prime[i]:
                prime_count += 1

        # Apply our game rule:
        # If the number of moves (prime_count) is odd, Maria wins.
        if prime_count % 2 == 1:
            maria_wins += 1
        # If the number of moves is even, Ben wins.
        else:
            ben_wins += 1

    # --- Step 4: Determine the Overall Winner ---
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        # If the scores are equal, it's a tie.
        return None
