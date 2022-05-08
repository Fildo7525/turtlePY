import turtle as tim

angle = 0
forward = 0

tim.listen()

def up():
	global angle, forward
	print("UP was hit angle: ", angle, " speed: ", forward)
	tim.setheading(angle)
	forward = forward + 10
	tim.forward(forward)

def down():
	global angle, forward
	print("DOWN was hit angle: ", angle, " speed: ", forward)
	tim.setheading(angle)
	forward = forward - 10
	tim.forward(forward)

def left():
	global angle, forward
	print("LEFT was hit angle: ", angle, " speed: ", forward)
	angle = angle-10
	tim.setheading(angle)
	tim.forward(forward)

def right():
	global angle, forward
	print("RIGHT was hit angle: ", angle, " speed: ", forward)
	angle = angle+10
	tim.setheading(angle)
	tim.forward(forward)

tim.onkey(up, "Up")  # This will call the up function if the "Left" arrow key is pressed
tim.onkey(down, "Down")
tim.onkey(left, "Left")
tim.onkey(right, "Right")

tim.mainloop()  # This will make sure the program continues to run 

