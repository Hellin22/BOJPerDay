scores = []
for i in range(5):
    total_score = sum(map(int, input().split()))
    scores.append(total_score)

winner = scores.index(max(scores)) + 1
max_score = max(scores)

print(winner, max_score)
