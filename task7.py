import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_simulations):
    sum_counts = {i: 0 for i in range(2, 13)}

    for _ in range(num_simulations):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        roll_sum = dice1 + dice2
        sum_counts[roll_sum] += 1

    return sum_counts

num_simulations = 1000000

sum_counts = simulate_dice_rolls(num_simulations)

sum_probabilities = {sum_: count / num_simulations for sum_, count in sum_counts.items()}

analytical_probabilities = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78,
}

print("| Сума | Ймовірність (Симульована) | Ймовірність (Аналітична) |")
print("|------|---------------------------|--------------------------|")
for sum_ in range(2, 13):
    print(f"| {sum_:>4} | {sum_probabilities[sum_]*100:>25.2f} | {analytical_probabilities[sum_]:>24.2f} |")

sums = list(sum_probabilities.keys())
simulated_probs = [sum_probabilities[sum_]*100 for sum_ in sums]
analytical_probs = [analytical_probabilities[sum_] for sum_ in sums]

x = range(len(sums))
plt.bar(x, simulated_probs, width=0.4, label='Симульована', align='center')
plt.bar(x, analytical_probs, width=0.4, label='Аналітична', align='edge')
plt.xlabel('Сума кісток')
plt.ylabel('Ймовірність (%)')
plt.title('Симульовані та аналітичні ймовірності сум кубиків')
plt.xticks(x, sums)
plt.legend()
plt.show()
