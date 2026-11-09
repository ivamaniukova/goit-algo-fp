import random

def monte_carlo_dice(num_rolls):
    if num_rolls <= 0:
        raise ValueError("Number of rolls must be a positive integer.")

    counts = {total: 0 for total in range(2, 13)}

    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2

        counts[total] += 1

    probabilities = {total: count / num_rolls for total, count in counts.items()}
    return counts, probabilities

if __name__ == "__main__":
    num_rolls = 100000
    counts, probabilities = monte_carlo_dice(num_rolls)

    analytical_probabilities = {
        2: 1/36,
        3: 2/36,
        4: 3/36,
        5: 4/36,
        6: 5/36,
        7: 6/36,
        8: 5/36,
        9: 4/36,
        10: 3/36,
        11: 2/36,
        12: 1/36
    }

    print(f"Results after {num_rolls} rolls:")
    print(
        f"{'Sum':<5} {'Count':>8} "
        f"{'Monte Carlo':>13} {'Analytical':>13} "
        f"{'Error (pp)':>12}"
    )
    print("-" * 55)

    max_error = 0

    for total in range(2, 13):
        simulated = probabilities[total] * 100
        exact = analytical_probabilities[total] * 100
        error = abs(simulated - exact)

        max_error = max(max_error, error)

        print(f"{total:<5} {counts[total]:>8} {simulated:>12.3f}% {exact:>12.3f}% {error:>12.3f}")

    print(f"\nMaximum absolute error: {max_error:.3f} percentage points")
