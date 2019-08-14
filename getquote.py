import random

def start():
    file = open("quotes.txt")
    quotes = file.readlines()
    file.close()

    random_number = random.randint(0, len(quotes)-1)
    print(quotes[random_number].rstrip())

    user_input = input("Enter your quote")
    if user_input.__len__() > 0:
        file = open("quotes.txt", "a")
        file.write("\n" + user_input)
        file.close()
    else:
        print("No user input")

if __name__ == "__main__":
    start()