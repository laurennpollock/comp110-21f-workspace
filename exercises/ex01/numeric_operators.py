"""Practicing numberic operators."""
__author__ = "730392344" 
left_hand_side: str = input("Left-hand side: ")
right_hand_side: str = input("Right-hand side: ")

exponentiation = int(left_hand_side) ** int(right_hand_side)
division = int(left_hand_side) / int(right_hand_side)
integer_division = int(left_hand_side) // int(right_hand_side)
remainder = int(left_hand_side) % int(right_hand_side) 
left_hand_side = str(left_hand_side)
right_hand_side = str(right_hand_side)
exponentiation = str(exponentiation)
division = str(division)
integer_division = str(integer_division)
remainder = str(remainder) 
print(left_hand_side + " ** " + right_hand_side + " is " + exponentiation)
print(left_hand_side + " / " + right_hand_side + " is " + division)
print(left_hand_side + " // " + right_hand_side + " is " + integer_division)
print(left_hand_side + " % " + right_hand_side + " is " + remainder)