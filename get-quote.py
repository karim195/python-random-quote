import random

def start():
    file = open("quotes.txt")
    quotes = file.readlines()
    file.close()

    random_number = random.randint(0, len(quotes)-1)
    print(quotes[random_number])


if __name__ == "__main__":
    start()