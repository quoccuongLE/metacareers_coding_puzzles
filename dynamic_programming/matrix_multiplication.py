# Recursive solution
def minimalMatrixMultiplication(N: list[int]) -> int:
    matrices = []
    for i in range(len(N) - 1):
        matrices.append([N[i], N[i+1]])

    def computeCost(matrices):
        if len(matrices) == 1:
            return 0
        if len(matrices) == 2:
            return matrices[0][0] * matrices[1][1]
        costs = []
        for i in range(1, len(N) - 1):
            cost = (
                computeCost(matrices[:i])
                + computeCost(matrices[i:])
                + matrices[0][0] * matrices[-1][1]
            )
            costs.append(cost)
        return min(costs)
    return computeCost(matrices)


if __name__ == "__main__":
    print(minimalMatrixMultiplication([2, 3, 1, 2]))
