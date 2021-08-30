"""Practicing numberic operators."""
__author__ = "730392344" 
left_hand_side: str = input("Left-hand side: ")
right_hand_side: str = input("Right-hand side: ")

line_one = int(left_hand_side) ** int(right_hand_side)
line_two = int(left_hand_side) / int(right_hand_side)
line_three = int(left_hand_side) // int(right_hand_side)
line_four = int(left_hand_side) % int(right_hand_side) 
left_hand_side = str(left_hand_side)
right_hand_side = str(right_hand_side)
line_one = str(line_one)
line_two = str(line_two)
line_three = str(line_three)
line_four = str(line_four) 
print(left_hand_side + " ** " + right_hand_side + " is " + line_one)
print(left_hand_side + " / " + right_hand_side + " is " + line_two)
print(left_hand_side + " // " + right_hand_side + " is " + line_three)
print(left_hand_side + " % " + right_hand_side + " is " + line_four)