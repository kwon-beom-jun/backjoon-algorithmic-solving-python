score = []
for i in range(8):
    score.append((int(input()), i+1))

score = sorted(score, reverse=True, key=lambda x: x[0])

print(sum(x[0] for x in score[:5]))

print(' '.join(str(x) for x in sorted(x[1] for x in score[:5])))