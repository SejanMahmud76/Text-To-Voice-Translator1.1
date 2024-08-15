import pyttsx3  # Import the pyttsx3 library for text-to-speech conversion

if __name__ == '__main__':
    # Welcome message
    print("Welcome to RoboSpeaker 1.1 created by Sezan")

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Infinite loop to continuously take user input
    while True:
        # Prompt the user to enter text
        x = input("Enter what you want to translate (type 'q' to quit):")

        # Check if the user wants to quit
        if x == "q":
            # Say goodbye message
            engine.say('bye bye friend')
            engine.runAndWait()
            break  # Exit the loop

        # Use the text-to-speech engine to say the entered text
        engine.say(x)
        engine.runAndWait()
