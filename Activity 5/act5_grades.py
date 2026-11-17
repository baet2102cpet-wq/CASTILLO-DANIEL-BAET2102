#DANIEL IVAN CASTILLO
#BAET 2102
#GRADE LIST ANALYZER

scores = []

for number in range(5):
    score = float(input("Enter quiz score " + str(number + 1) + ": "))
    scores.append(score)

scores.sort()

highest_score = scores[-1]
lowest_score = scores[0]
average_score = round(sum(scores) / len(scores), 1)

print("Sorted scores:", scores)
print("Highest score:", highest_score)
print("Lowest score:", lowest_score)
print("Average score:", format(average_score, ".1f"))
