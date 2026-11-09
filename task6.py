items = {
  "pizza": {"cost": 50, "calories": 300},
  "hamburger": {"cost": 40, "calories": 250},
  "hot-dog": {"cost": 30, "calories": 200},
  "pepsi": {"cost": 10, "calories": 100},
  "cola": {"cost": 15, "calories": 220},
  "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    if budget < 0:
        raise ValueError("Budget cannot be negative")
    sorted_items = sorted(items, key=lambda name: items[name]["calories"] / items[name]["cost"], reverse=True)
    selected_items = []

    for name in sorted_items:
        cost = items[name]["cost"]
        if cost <= budget:
            selected_items.append(name)
            budget -= cost
    return selected_items

def dynamic_programming(items, budget):
    if budget < 0:
        raise ValueError("Budget cannot be negative")
    n = len(items)
    item_names = list(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name = item_names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name = item_names[i - 1]
            selected_items.append(name)
            w -= items[name]["cost"]

    selected_items.reverse()
    return selected_items

if __name__ == "__main__":
    budget = 100
    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    for title, result in [("Greedy", greedy_result), ("Dynamic Programming", dp_result)]:
        total_cost = sum(items[name]["cost"] for name in result)
        total_calories = sum(items[name]["calories"] for name in result)
        print(f"{title} algorithm selected items: {result}")
        print(f"Total cost: {total_cost}, Total calories: {total_calories}\n")