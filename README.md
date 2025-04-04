Moodbot is an interactive web application that detects the emotion behind a user’s message and responds in a way that matches their mood. It’s designed to act like a mini emotional companion—you type something in, and Moodbot figures out if you’re feeling happy, sad, or neutral, then responds with a thoughtful or uplifting message. It's a great mix of sentiment analysis, conversational AI, and large language model (LLM) integration, built with Python, Flask, and natural language processing (NLP).

The backend taps into a trained sentiment analysis model that identifies emotional tones such as joy, sadness, fear, and more. But it doesn't stop at detection—Moodbot goes a step further by making the response feel personal. If you're down, it may send you a reassuring message or comforting words. If you're excited, it cheers you on. This gives the app a sense of being emotionally aware, not just analytical.

To process user input, the app first runs the text through a preprocessing pipeline: converting everything to lowercase, removing punctuation, filtering out common stopwords, and lemmatizing words so the model can better understand the core meaning. The cleaned text is then passed to the trained model, which classifies the emotion and triggers an appropriate response.

For generating rich, human-like replies, Moodbot also integrates the Gemini API—a powerful language model from Google. Once an emotion is detected, Gemini helps craft more dynamic, empathetic, and engaging responses tailored to that emotion. This allows Moodbot to blend rule-based sentiment classification with the creativity and flexibility of an LLM, improving the quality of conversations and enhancing the user experience.

The model was trained using the Emotions Dataset for NLP available on Kaggle: https://www.kaggle.com/datasets/praveengovi/emotions-dataset-for-nlp. Specifically, the training text data file from this dataset was used to teach the model how to recognize a range of emotions.

The project is modular and well-organized:

server.py manages the Flask server and application routes.

preprocessing_py.py handles text preprocessing and cleanup.

SentimentAnalysis/ contains the trained model and related utilities.

Basic HTML templates make up the frontend for user interaction.

Moodbot is a beginner-friendly project that illustrates how emotional intelligence can be embedded into software. It’s ideal for those exploring NLP, Flask development, sentiment analysis, or chatbot building. You can easily extend the project by supporting additional emotions (like anger or surprise), improving the model’s accuracy, or making responses even more nuanced with further Gemini API prompts.

Whether you're diving into AI or just want to create a simple but emotionally aware chatbot, Moodbot is a great place to start!
