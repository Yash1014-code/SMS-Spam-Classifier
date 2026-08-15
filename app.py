import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Page configuration
st.set_page_config(
    page_title="SMS Spam Classifier",
    page_icon="📱"
)

# Title
st.title("📱 SMS Spam Classifier")

st.write("Enter an SMS below to check whether it is Spam or Ham.")

# Text input
message = st.text_area(
    "Enter your message:",
    placeholder="Example: Congratulations! You won a free prize...",
    height=150
)

# Buttons
col1, col2 = st.columns(2)

with col1:
    analyze = st.button(
        "🔍 Analyze",
        use_container_width=True,
        type="primary"
    )

with col2:
    clear = st.button(
        "🗑️ Clear",
        use_container_width=True
    )

# Clear button
if clear:
    st.rerun()

# Analyze button
if analyze:

    if message.strip() == "":
        st.warning("Please enter a message.")

    else:
        # Convert text into TF-IDF features
        message_vector = vectorizer.transform([message])

        # Prediction
        prediction = model.predict(message_vector)[0]

        # Prediction probabilities
        probabilities = model.predict_proba(message_vector)[0]

        ham_probability = probabilities[0] * 100
        spam_probability = probabilities[1] * 100

        st.divider()

        # Result
        if prediction == 1:

            st.error("🚨 This message is SPAM")

            st.metric(
                "Spam Probability",
                f"{spam_probability:.2f}%"
            )

            st.progress(
                int(spam_probability)
            )

        else:

            st.success("✅ This message is HAM")

            st.metric(
                "Ham Probability",
                f"{ham_probability:.2f}%"
            )

            st.progress(
                int(ham_probability)
            )