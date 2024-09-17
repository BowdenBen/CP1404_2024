"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
while 0 < score <= 100:
    if 90 <= score < 100:
        print("Excellent")
    elif 50 <= score < 90:
        print("Passable")
    else :
        print("Poor")
print("Invalid Score")