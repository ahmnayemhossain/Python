print("Welcome to the Student Score Analyzer!")

scores_text = input("Enter student scores separated by spaces: ")
scores = [int(score) for score in scores_text.split()]

sorted_scores = sorted(scores)
lowest_score = min(scores)
highest_score = max(scores)
average_score = sum(scores) / len(scores)

print(f"Sorted scores: {sorted_scores}")
print(f"Lowest score: {lowest_score}")
print(f"Highest score: {highest_score}")
print(f"Average score: {average_score:.2f}")
