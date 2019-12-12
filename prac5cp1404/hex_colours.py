
def main():
    user_input = (input("Enter Colour Name:")).lower()
    color(user_input)

def color(user_input):
    dict = {'darkgoldenrod': "#b8860b", 'aliceblue': "#f0f8ff", 'azure1': "#f0ffff", "aquamarine1": "#7fffd4", "blanchedalmond": "#ffebcd", "brown2": "#ee3b3b", "burlywood": "	#deb887", "cadetblue": "#5f9ea0","cornflowerblue": "#6495ed", "cornsilk4": "#8b8878"}
    if user_input in dict:
        print(dict[user_input])
        main()

    elif user_input == " " or user_input == "":
        exit()

    else:
        print("False")
        main()

main()