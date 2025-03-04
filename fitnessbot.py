import streamlit as st
import random

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return f"Your BMI is **{bmi:.2f}**. You are **Underweight**. Consider a balanced diet."
    elif 18.5 <= bmi < 24.9:
        return f"Your BMI is **{bmi:.2f}**. You are at a **Healthy weight**. Keep it up!"
    elif 25 <= bmi < 29.9:
        return f"Your BMI is **{bmi:.2f}**. You are **Overweight**. Try regular exercise and a balanced diet."
    else:
        return f"Your BMI is **{bmi:.2f}**. You are **Obese**. Consider consulting a health professional."

# Workout and Diet Suggestions
workout_plans = {
    "weight loss": ["Cardio (Running, Cycling)", "HIIT Workouts", "Jump Rope"],
    "muscle gain": ["Weight Lifting", "Bodyweight Exercises", "Progressive Overload"],
    "flexibility": ["Yoga", "Stretching", "Pilates"],
    "general fitness": ["Walking", "Swimming", "Light Cardio"]
}

diet_plans = {
    "weight loss": ["Lean protein", "Vegetables", "Low-carb diet"],
    "muscle gain": ["High protein diet", "Healthy fats", "Complex carbs"],
    "flexibility": ["Balanced diet", "Hydration", "Anti-inflammatory foods"],
    "general fitness": ["Fruits", "Nuts", "Whole grains"]
}

# Chatbot Responses
def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if "bmi" in user_input:
        return "Sure! Enter your **weight (kg)** and **height (m)** below, and I'll calculate it for you."
    
    elif "workout" in user_input or "exercise" in user_input:
        return "What is your fitness goal? (Weight Loss, Muscle Gain, Flexibility, General Fitness)"
    
    elif "diet" in user_input or "nutrition" in user_input:
        return "What is your fitness goal? (Weight Loss, Muscle Gain, Flexibility, General Fitness)"
    
    elif user_input in workout_plans:
        workouts = "\n".join([f"- {w}" for w in workout_plans[user_input]])
        return f"🏋️ Recommended Workouts for **{user_input.capitalize()}**:\n{workouts}"
    
    elif user_input in diet_plans:
        diet = "\n".join([f"- {d}" for d in diet_plans[user_input]])
        return f"🥗 Recommended Diet for **{user_input.capitalize()}**:\n{diet}"
    
    else:
        return random.choice([
            "I'm here to help! You can ask about **BMI, workouts, or diet plans**.",
            "Can you please clarify? I can assist with fitness, health, and nutrition!"
        ])

# Streamlit UI
st.title("💬 Fitness Chatbot")
st.write("Ask me anything about **fitness, workouts, BMI, or diet!**")

# Chat Interface
user_query = st.text_input("You:", "")

if user_query:
    bot_reply = chatbot_response(user_query)
    st.text_area("Bot:", bot_reply, height=100)

    # If BMI is asked, show input fields
    if "bmi" in user_query:
        weight = st.number_input("Enter your weight (kg)", min_value=1.0)
        height = st.number_input("Enter your height (m)", min_value=0.5, format="%.2f")
        if st.button("Calculate BMI"):
            if weight and height:
                st.success(calculate_bmi(weight, height))
            else:
                st.warning("Please enter valid weight and height!")
