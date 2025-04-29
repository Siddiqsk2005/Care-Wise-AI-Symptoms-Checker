import google.generativeai as palm


palm.configure(api_key='AIzaSyD8GHsKbb5D3K1Oi15tpr0IHImDoNVGJic')  


def list_available_models():
    """List available models in the project and return them as a list."""
    try:
        models = list(palm.list_models())  
        print("✅ Available Models:\n")
        for model in models:
            print(f"Model Name: {model.name}\nDescription: {model.description}\n")
        return models
    except Exception as e:
        print(f"❌ Error listing models: {str(e)}")
        return []


def get_symptom_advice(symptom_description, model_name):
    """Generate medical advice based on the given symptom description."""
    try:
        model = palm.GenerativeModel(model_name)
        response = model.generate_content(symptom_description)
        return response.text if response else "⚠️ No advice generated."
    except Exception as e:
        return f"❌ An error occurred: {str(e)}"


if __name__ == "__main__":
    # Step 1: List available models
    models = list_available_models()

    if not models:
        print("\n❗ No models available. Please check your credentials or GCP settings.")
    else:
        # Step 2: Select the best available model
        preferred_model = next(
            (m.name for m in models if 'gemini-1.5-pro-latest' in m.name), models[0].name
        )
        print(f"\n✨ Using model: {preferred_model}\n")

        # Step 3: Ask for user input and generate advice
        user_input = input("💬 Describe your symptoms: ")
        advice = get_symptom_advice(user_input, preferred_model)
        print("\n💡 AI's Suggestion:\n", advice)
