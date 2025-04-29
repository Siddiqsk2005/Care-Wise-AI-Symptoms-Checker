import google.generativeai as palm

# Configure the API key for PaLM (replace with your actual API key)
palm.configure(api_key="YOUR_API_KEY")

def get_palm_response(symptoms_text):
    """
    Generates a medical response using the PaLM Chat Bison model for given symptoms.
    """
    try:
        # Create a chat session and get response
        response = palm.chat(
            model="models/chat-bison-001",
            context=(
                "You are a medical assistant that provides possible diagnoses and treatment recommendations "
                "based on the symptoms provided by the patient. Respond clearly and concisely."
            ),
            messages=[f"Patient reports: {symptoms_text}. Suggest possible diagnoses and treatments."],
            temperature=0.2,
        )
        return response.last

    except Exception as e:
        return f"An error occurred while fetching the response: {str(e)}"

if __name__ == "__main__":
    # Example usage
    symptoms = input("Enter patient symptoms: ")
    response = get_palm_response(symptoms)
    print("\nAI-Powered Diagnosis and Treatment Suggestions:\n", response)
