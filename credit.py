credit_score = int(input("Enter your credit score: "))

if credit_score >= 740:
    print("Excellent credit")
elif credit_score >= 670:
    print("Good credit")
elif credit_score >= 580:
    print("Fair credit")
else:
    print("Poor credit")