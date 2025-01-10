from typing import Dict
import re

def mood_tracker():
    """
    A simple mood tracker chatbot using dictionaries and sentence input.
    Allows user to share thoughts after expressing willingness to talk.
    """

    moods = {
        "happy": ["happy", "joyful", "excited", "delighted", "content", "best"],
        "sad": ["sad", "unhappy", "depressed", "down", "gloomy", "worst", "disappointed"],
        "angry": ["angry", "mad", "frustrated", "furious", "pissed off"],
        "neutral": ["neutral", "okay", "fine", "alright", "indifferent", "bored"],
        "overwhelmed": ["overload", "overburden"],
        "annoyed": ["irritated", "fed up", "annoy", "tired"]
    }

    mood_responses = {
        "happy": "That's fantastic! Keep the good vibes going!",
        "sad": "I'm sorry to hear that. Is there anything I can do to help?",
        "angry": "Take a deep breath. Let's try to find a way to calm down.",
        "neutral": "Okay, thanks for sharing.",
        "tired": "Maybe it's time for some rest and relaxation.",
        "excited": "Woohoo! Share the excitement!",
        "anxious": "It's okay to feel anxious. Let's try some relaxation techniques.",
        "stressed": "Let's find some ways to de-stress. Maybe some exercise or meditation?",
        "frustrated": "lets listen to some music?",
        "bored": "lets play a quize game",
    }

    while True:
        user_input = input("How are you feeling today? (Enter a sentence or 'quit' to exit): ")

        if user_input.lower() == "quit":
            break

        detected_mood = None
        for mood, keywords in moods.items():
            for keyword in keywords:
                if re.search(r"\b" + keyword + r"\b", user_input, re.IGNORECASE):
                    detected_mood = mood
                    break
            if detected_mood:
                break

        if detected_mood:
            print(mood_responses.get(detected_mood, "I'm not sure how to respond to that."))  # Print the detected mood response
            print(f"I think you're feeling {detected_mood}.")
            user_input = input("Would you like to talk about it? (yes/no): ")
            if user_input.lower() == "yes":
                print("I'm here to listen. Please feel free to share what's on your mind.")
                user_thoughts = input("What are your thoughts or feelings about this? ")
                print(f"Thank you for sharing. I understand that you're feeling {detected_mood} and {user_thoughts}.")
                print("Remember, it's okay to feel this way. Take things one step at a time and prioritize your well-being.")
            else:
                print("Okay, I respect your privacy. If you change your mind, I'm here for you.")
        else:
            print("I'm not sure how you're feeling. Please try again.")

if __name__ == "__main__":
    mood_tracker()
