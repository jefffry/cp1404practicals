def main():
    score = float(input("Enter score :"))
    print(user_score(score))
def user_score(score):
    if score < 0 or score > 100:
        return "Invalid Score"

    elif score >= 50 and score <= 90:
        return "Passable"
    elif score > 90 and score <= 100:
        return "Excellent"
    else:
        return "Bad"
main()
