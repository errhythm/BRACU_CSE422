import random

# student_id = input("Enter your student ID: ")
student_id = "22241163"

student_id = student_id.replace("0", "8")

# get the 5th min_points of the student_id
min_points = student_id[4]
# print("Minimum points the Optimus Prime can achieve from the game =", min_points)

total_points = student_id[-2:][::-1]
# print("Total points to win = ", total_points)

max_points = round(float(total_points) * 1.5)
# print("Maximum points the Optimus Prime can achieve from the game =", max_points)


shuffle = student_id[3]
# print("Shuffle the deck", shuffle, "times")

random_numbers = []
for i in range(8):
    random_numbers.append(random.randint(int(min_points), int(max_points)))
print("Generated 8 random points between the minimum and maximum point limits:", random_numbers)
print("Total points to win", total_points)


def alpha_beta_pruning(random_numbers, total_points, shuffle):
    # sort the random_numbers in ascending order
    random_numbers.sort()
    # print("Sorted random numbers:", random_numbers)

    # shuffle the deck
    for i in range(int(shuffle)):
        random.shuffle(random_numbers)
    # print("Shuffled random numbers:", random_numbers)

    # remove the first 3 elements from the list
    random_numbers = random_numbers[3:]
    # print("Removed first 3 elements from the list:", random_numbers)

    # remove the last 3 elements from the list
    random_numbers = random_numbers[:-3]
    # print("Removed last 3 elements from the list:", random_numbers)

    # sum the remaining elements in the list
    sum = 0
    for i in random_numbers:
        sum += i
    # print("Sum of the remaining elements in the list:", sum)

    # check if sum is greater than total_points
    if sum > int(total_points):
        print("Sum of the remaining elements in the list is greater than total points to win")
    else:
        print("Sum of the remaining elements in the list is less than total points to win")

    return sum

achieved_points = alpha_beta_pruning(random_numbers, total_points, shuffle)
print("Achieved points =", achieved_points)
if achieved_points >= int(total_points):
    print("Winner is Optimus Prime")
else:
    print("Winner is Megatron")
