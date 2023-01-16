# bounce.py
#
# Exercise 1.5

ball_height = 100
bounce_coeff = 3/5
bounce_num = 0

for i in range(10):
	bounce_num = bounce_num + 1
	ball_height = ball_height * bounce_coeff
	print(bounce_num, round(ball_height,4))
