def mad_libs():
    # Create a story with placeholders for the missing words
    story = "Once upon a time, there was a {} {} who lived in a {}. Every day, they would {}. One day, they decided to {}. As they {}, they saw a {}. It was a {}! The {} was very {}. They {} away as fast as they could."

    # Get user input for each placeholder
    noun1 = input("Enter a noun: ")
    adjective1 = input("Enter an adjective: ")
    place = input("Enter a place: ")
    verb1 = input("Enter a verb: ")
    verb2 = input("Enter another verb: ")
    verb3 = input("Enter yet another verb: ")
    noun2 = input("Enter a noun: ")
    animal = input("Enter an animal: ")
    animal_name = input("Enter a name for the animal: ")
    adjective2 = input("Enter another adjective: ")
    verb4 = input("Enter a verb: ")

    # Fill in the story with user input
    filled_story = story.format(noun1, adjective1, place, verb1, verb2, verb3, noun2, animal, animal_name, adjective2, verb4)

    # Print the filled-in story
    print("\nHere's your Mad Libs story:\n")
    print(filled_story)


# Call the function to play the game
if __name__ == "__main__":
    mad_libs()
