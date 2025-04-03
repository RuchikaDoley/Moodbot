import google.generativeai as genai
from textblob import TextBlob
import os

# -------- CONFIG --------
GOOGLE_API_KEY = os.getnenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
chat = genai.GenerativeModel("gemini-1.5-flash-002").start_chat()

# -------- EMOTION DETECTION --------
emotion_keywords = {
    "joy": ["happy", "excited", "great", "awesome", "joy", "glad", "delighted", "ecstatic", "love"],
    "sadness": ["sad", "down", "depressed", "unhappy", "miserable", "crying", "blue"],
    "anger": ["angry", "mad", "furious", "frustrated", "annoyed", "hate", "irritated"],
    "fear": ["afraid", "scared", "fear", "nervous", "worried", "anxious"],
}

def detect_emotion(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    lower_text = text.lower()

    # Keyword-based classification
    for emotion, keywords in emotion_keywords.items():
        if any(word in lower_text for word in keywords):
            return emotion

    # Polarity-based fallback
    if polarity > 0.3:
        return "joy"
    elif polarity < -0.4:
        return "sadness"
    else:
        return "neutral"

# -------- SYSTEM PROMPT BASED ON EMOTION --------
def get_emotion_prompt(emotion):
    prompts = {
        "joy": "You are cheerful, upbeat, and playful. Celebrate the user's happiness and match their excitement.",
        "sadness": "You are gentle and compassionate. Be a good listener, validate their feelings, and offer comforting responses.",
        "anger": "You are calm and patient. Help the user process their anger without judgment, and gently guide them toward understanding and peace.",
        "fear": "You are reassuring and supportive. Ease the user's worries, validate their fears, and offer calming perspectives.",
        "neutral": "You are thoughtful and balanced. Keep the conversation open and engaging without taking a strong emotional stance."
    }
    return prompts[emotion]

# -------- CHAT HANDLER --------
def generate_response(user_input):
    emotion = detect_emotion(user_input)
    system_prompt = get_emotion_prompt(emotion)

    # Send mood-aligned system prompt once
    chat.send_message(system_prompt)

    # Send user input
    response = chat.send_message(user_input)

    return emotion, response.text

# -------- MAIN LOOP --------
def main():
    print("🧠 Emotion-Aware Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            print("Bot: Wishing you well! 👋")
            break

        emotion, reply = generate_response(user_input)
        print(f"[Detected Emotion: {emotion}]")
        print(f"Bot: {reply}")

if __name__ == "__main__":
    main()
