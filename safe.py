def health_info(condition):
    precautions = {
        "cold": [
            "Stay hydrated with warm fluids",
            "Get plenty of rest",
            "Use a humidifier to ease congestion",
            "Avoid cold drinks and exposure to cold weather"
        ],
        "fever": [
            "Stay hydrated with water and electrolytes",
            "Rest as much as possible",
            "Use a cool compress to reduce temperature",
            "Wear light clothing to help regulate body heat"
        ]
    }

    tablets = {
        "cold": ["Paracetamol", "Cetirizine", "Levocetirizine"],
        "fever": ["Paracetamol", "Ibuprofen"]
    }

    if condition.lower() in precautions:
        print(f"Precautions for {condition.capitalize()}:")
        for item in precautions[condition.lower()]:
            print(f"- {item}")
        print(f"\nCommon Tablets for {condition.capitalize()}:")
        for med in tablets[condition.lower()]:
            print(f"- {med}")
    else:
        print("Sorry, information for this condition is not available.")

# Example usage
condition = input("Enter the condition (cold/fever): ")
health_info(condition)
