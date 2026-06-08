print("Day 19 practice exercises")

print("\nExercise 1: List sorting")
numbers = [9, 2, 7, 1]
numbers.sort()
print(numbers)

print("\nExercise 2: Minimum and maximum")
print(min(numbers))
print(max(numbers))

print("\nExercise 3: Append and remove")
numbers.append(10)
numbers.remove(2)
print(numbers)

print("\nExercise 4: User score list")
score_one = int(input("Enter score 1: "))
score_two = int(input("Enter score 2: "))
score_three = int(input("Enter score 3: "))
score_list = [score_one, score_two, score_three]
print(sorted(score_list))

print("\nExercise 5: Sum and average")
total_score = sum(score_list)
average_score = total_score / len(score_list)
print(total_score)
print(f"{average_score:.2f}")
