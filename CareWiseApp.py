import streamlit as st
import google.generativeai as palm


palm.configure(api_key='AIzaSyCLQTE7MsiJd0KJckm0kLRFzROUCC0BMbQ')  

def list_available_models():
    """List available models in the project and return them as a list."""
    try:
        models = list(palm.list_models())  
        return models
    except Exception as e:
        st.error(f"❌ Error listing models: {str(e)}")
        return []

def get_symptom_advice(symptom_description, model_name):
    """Generate medical advice based on the given symptom description."""
    try:
        model = palm.GenerativeModel(model_name)
        response = model.generate_content(symptom_description)
        return response.text if response else "⚠️ No advice generated."
    except Exception as e:
        return f"❌ An error occurred: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="CareWise AI", page_icon="🏥", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .header {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        color: #4CAF50;
    }
    .stSuccess {
        background-color: #20B2AA; /* Light Sea Blue */
        color: white;
        padding: 16px; /* Increased padding */
        border-radius: 8px;
        border: 1px solid #20B2AA;
        font-size: 18px; /* Increased font size */
        line-height: 1.6; /* Improved line spacing */
        margin-top: 10px; /* Added margin for spacing */
    }
    </style>
""", unsafe_allow_html=True)

# Header section with an engaging background and icon
st.markdown('<div class="header">🏥 CareWise AI </div>', unsafe_allow_html=True)

# Info section with a clear description and icon
st.markdown("""
    <p style="font-size: 18px; text-align: center; color: #555;">Describe your symptoms below, and get personalized medical advice from our AI system powered by Google's Generative AI.</p>
    <div style="text-align: center;">
        <span style="font-size: 48px;">🩺</span>
    </div>
""", unsafe_allow_html=True)

# User input for symptoms with a styled text area
user_input = st.text_area(
    "💬 Describe your symptoms:",
    "",
    height=150,
    max_chars=500,
    help="Please provide as much detail as possible for accurate advice.",
    placeholder="Example: I have a fever, headache, and body aches..."
)

# Stylish button to trigger advice generation
if st.button("Get Medical Advice", use_container_width=True):
    if user_input:
        # Show loading spinner while processing the request
        with st.spinner("🔍 Generating advice... Please wait."):
            # Show available models
            models = list_available_models()

            if models:
                # Select model from the list (default to the first model)
                preferred_model = next(
                    (m.name for m in models if 'gemini-1.5-pro-latest' in m.name), models[0].name
                )

                st.write(f"✨ Using model: {preferred_model}")

                # Get AI advice based on the user's symptoms
                advice = get_symptom_advice(user_input, preferred_model)
                st.subheader("💡 AI's Suggestion:")
                st.markdown(f'<div class="stSuccess">{advice}</div>', unsafe_allow_html=True)  # Light Sea Blue background
            else:
                st.error("❌ No models available. Please check your credentials or GCP settings.")
    else:
        st.warning("⚠️ Please enter your symptoms for analysis.")

# Footer with some extra information and contact
st.markdown("""
    <hr>
    <p style="text-align: center; font-size: 14px; color: #777;">
        Powered by <a href="https://cloud.google.com/ai" target="_blank">Google Cloud AI</a> | Designed for quick medical assistance.
    </p>
""", unsafe_allow_html=True)