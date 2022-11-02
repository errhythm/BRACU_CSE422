import random

# student_id = input("Enter your student ID: ")
student_id = "25485465"

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

# random_numbers = []
# for i in range(8):
#     random_numbers.append(random.randint(int(min_points), int(max_points)))
# print("Generated 8 random points between the minimum and maximum point limits:", random_numbers)
# print("Total points to win", total_points)

random_numbers = [66, 74, 14, 73, 19, 26, 32, 40]
print("Generated 8 random points between the minimum and maximum point limits:", random_numbers)


def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]
    if maximizingPlayer:
        best = -1000

        # Recur for left and right children
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break

        return best

    else:
        best = 1000

        # Recur for left and right children
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break
        return best


print("Total points to win:", total_points)
print("Achieved point by applying alpha-beta pruning =", minimax(0, 0, True, random_numbers, -1000, 1000))
if minimax(0, 0, True, random_numbers, -1000, 1000) >= int(total_points):
    print("The Winner is Optimus Prime")
else:
    print("The Winner is Megatron")
