def team_weights(weights):
    even_index = [weights[i] for i in range(len(weights)) if i % 2 == 0]
    odd_index = [weights[i] for i in range(len(weights)) if i % 2 == 1]
    total1 = sum(even_index)
    total2 = sum(odd_index)
    return (total1, total2)
