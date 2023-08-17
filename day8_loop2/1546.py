import sys

N = int(sys.stdin.readline())
old_scores = list(map(int, sys.stdin.readline().split()))
M = max(old_scores)

new_scores = []
for score in old_scores:
    new_scores.append(score / M * 100)

print(sum(new_scores) / N)
