# this problem is solved by chagGPT4
# https://chat.openai.com/c/08105f7c-ab04-4196-aa61-17b03fb7b835

# data
physics_scores = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history_scores = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

n = len(physics_scores)

# Calculate Σx, Σy, Σx^2, Σy^2, Σxy
sum_x = sum(physics_scores)
sum_y = sum(history_scores)
sum_x2 = sum([x**2 for x in physics_scores])
sum_y2 = sum([y**2 for y in history_scores])
sum_xy = sum([x*y for x, y in zip(physics_scores, history_scores)])


# Apply the formula
numerator = n * sum_xy - sum_x * sum_y
denominator = ((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))**0.5

r = numerator / denominator

print(round(r, 3))
