"""Demonstrating the use of relational operators."""

__author__ = "730459528"

left_hand: str = input ("What is the value for the left-hand side? ")
right_hand: str = input ("What is the value for the right-hand side? ")
left_hand_side = int(left_hand)
right_hand_side = int(right_hand)
print(left_hand + " < " + right_hand + " is " + (str(left_hand_side < right_hand_side)))
print(left_hand + " >= " + right_hand + " is " + (str(left_hand_side >= right_hand_side)))
print(left_hand + " == " + right_hand + " is " + (str(left_hand_side == right_hand_side)))
print(left_hand + " != " + right_hand + " is " + (str(left_hand_side != right_hand_side)))