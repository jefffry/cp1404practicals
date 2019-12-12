
def main():
    user_input = (input("Enter Colour Name:")).lower()
    color(user_input)

def color(user_input):
    dict = {'darkgoldenrod': "#b8860b", 'aliceblue': "#f0f8ff", 'azure1': "#f0ffff", "aquamarine1": "#7fffd4", "blanchedalmond": "#ffebcd", "brown2": "#ee3b3b", "burlywood": "	#deb887", "cadetblue": "#5f9ea0","cornflowerblue": "#6495ed", "cornsilk4": "#8b8878"}
    while user_input !="":
        if user_input in dict:
            print(dict[user_input])
            user_input = input("Enter Colour Name").lower()
        else:
            print("Invalid color name")
            user_input = input("Enter Colour Name").lower()


main()