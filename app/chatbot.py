def get_response(message: str) -> str:
    message = message.lower()

    if "symptom" in message or "track" in message:
        return "You can log symptoms like acne, fatigue, cramps, and mood swings using the PCOSBuddy tracker."
    elif "diet" in message:
        return "A low-GI diet with balanced protein and fiber can help manage PCOS symptoms. Would you like some meal suggestions?"
    elif "exercise" in message:
        return "Moderate workouts like cycling, yoga, or walking for 30 mins a day are helpful for PCOS."
    elif "hello" in message or "hi" in message:
        return "Hi! I’m your PCOSBuddy Chatbot. How can I help you today?"
    else:
        return "I'm still learning! For detailed support, please talk to a health expert or check our symptom guide."
