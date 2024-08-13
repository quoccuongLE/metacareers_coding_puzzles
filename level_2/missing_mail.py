from typing import List

# Write any import statements here
# Dynamic Programming

def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
    # Keep track of the best trajectory, where i is the number of days without pickup
    # Keep track of both the potential value for next pickup, and current profit
    best_traj = [(0.0, 0.0)]

    for price in V:
        # print(price, best_traj)
        # Add the new day : (expected value to be picked up, final expected value)
        best_traj.insert(0, (0.0, 0.0))

        # Update the best trajectories so far for the new day, considering the packages could've stolen
        best_traj = [(p * (1 - S), f) for p, f in best_traj]

        # Possibility #1 : pickup that day
        # in this case, find the best possible choice among all saved so far (just keep the best one)
        val = max(f + p for p, f in best_traj) + price - C
        best_traj[0] = (0.0, val)

        # Possibility #2 : don't pickup
        # In this case, update the on-going price
        for i in range(1, len(best_traj)):
            p, f = best_traj[i]
            best_traj[i] = (p + price, f)

        # print(best_traj, "\n==========")

    return round(max(f for p, f in best_traj), 5)


if __name__ == "__main__":
    assert 20.10825 == getMaxExpectedProfit(N=5, V=[10, 2, 8, 6, 4], C=3, S=0.15)
    # assert 17.0 == getMaxExpectedProfit(N=5, V=[10, 2, 8, 6, 4], C=3, S=0.5)
