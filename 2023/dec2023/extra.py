def min_infected_cows(n, state):
    min_infected = float('inf')

    for i in range(n):
        nights = state.count('1')  # Initial infected cows
        infected = [False] * n
        infected[i] = True  # Patient zero

        while True:
            new_infected = [False] * n
            for j in range(n):
                if infected[j]:
                    nights += 1
                    if j > 0:
                        new_infected[j - 1] = True
                    if j < n - 1:
                        new_infected[j + 1] = True

            if not any(new_infected):
                break  # No new infections in this night

            infected = new_infected

        min_infected = min(min_infected, nights)

    return min_infected

# Example usage:
# Read input
# n = int(input())
# state = input().strip()

# Sample inputs
n1 = 5
state1 = "11111"
print(min_infected_cows(n1, state1))  # Output: 1

n2 = 6
state2 = "011101"
print(min_infected_cows(n2, state2))  # Output: 4
