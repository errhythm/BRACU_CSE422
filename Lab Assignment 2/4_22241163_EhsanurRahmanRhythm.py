import random

student_id = input("Enter student ID: \n")
student_id = student_id.replace("0", "8")
min_points = student_id[4]
total_points = student_id[-2:][::-1]
max_points = round(float(total_points) * 1.5)

random_numbers = []

for i in range(8):
    random_numbers.append(random.randint(int(min_points), int(max_points)))


print("Generated 8 random points between the minimum and maximum point limits:", random_numbers)
print("Total points to win:", total_points)


def alphabeta(depth, index, points, alpha, beta, maximize):
    if depth == 3:
        return points[index]
    if maximize:
        bestval = -1000
        for i in range(0, 2):
            value = alphabeta(depth + 1, index * 2 + i, points, alpha, beta, False)
            bestval = max(bestval, value)
            alpha = max(alpha, bestval)
            if beta <= alpha:
                break
        return bestval

    else:
        bestval = 1000
        for i in range(0, 2):
            value = alphabeta(depth + 1, index * 2 + i, points, alpha, beta, True)
            bestval = min(bestval, value)
            beta = min(beta, bestval)
            if beta <= alpha:
                break
        return bestval


print("Achieved point by applying alpha-beta pruning =", alphabeta(0, 0, random_numbers, -1000, 1000, True))

if alphabeta(0, 0, random_numbers, -1000, 1000, True) >= int(total_points):
    print("The Winner is Optimus Prime\n")
else:
    print("The Winner is Megatron\n")

print("After the shuffle: ")
shuffle_result = []
win = 0

shuffle = student_id[3]

for i in range(int(shuffle)):
    random.shuffle(random_numbers)
    shuffle_result.append(alphabeta(0, 0, random_numbers, -1000, 1000, True))
    if alphabeta(0, 0, random_numbers, -1000, 1000, True) >= int(total_points):
        win += 1

print("List of all points values from each shuffle:", shuffle_result)
print("The maximum value of all shuffles:", max(shuffle_result))
print("Won", win, "times out of", shuffle, "number of shuffles")
