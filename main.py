import random


def main():
    movieQuotes = {
        "Houston, we have a problem.": "Apollo 13",
        "I'll be back.": "Terminator",
        "Remember who you are.": "The Lion King",
        "I'm the king of the world!": "Titanic",
        "There's no place like home.": "The Wizard of Oz",
        "Bond. James Bond.": "Dr. No",
        "A martini. Shaken, not stirred.": "Goldfinger",
        "I see dead people.": "The Sixth Sense",
        "It's alive! It's alive!": "Frankenstein",
        "I feel the need - the need for speed!": "Top Gun"
    }

    # Ask for input and convert to integer
    numQuestions = input("How many questions would you like? ")
    numQuestions = int(numQuestions)

    # If input is greater than length of dictionary, exit program
    if numQuestions > len(movieQuotes):
        print("Invalid number of questions.")
        exit()

    # Create random list
    randomQuotes = random.sample(list(movieQuotes), numQuestions)

    # Score variable to hold total number of correct answers
    score = 0

    # Loop through each element in randomQuotes
    for q in randomQuotes:
        print(f"Question #{randomQuotes.index(q) + 1} From what movie is the following quote?")
        print(f"\"{q}\"")
        answer = input("Your Answer: ")

        # Convert user input and answer to lowercase and compare
        if answer.lower() == movieQuotes[q].lower():
            print("Correct!")

            # If answer is correct increment score by one
            score += 1

        # Else display the correct answer
        else:
            print(f"Incorrect! The correct answer is: {movieQuotes[q]}")
        print()

    # Display final score
    print(f"You answered {score} out of {len(randomQuotes)} correctly.")


# Call main
if __name__ == '__main__':
    main()
