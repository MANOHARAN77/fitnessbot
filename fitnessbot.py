import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        status = "Underweight"
    elif 18.5 <= bmi < 24.9:
        status = "Normal weight"
    elif 25 <= bmi < 29.9:
        status = "Overweight"
    else:
        status = "Obese"
    return bmi, status

# Function to suggest workouts
def suggest_workout(goal):
    workouts = {
        "Weight Loss": ["Cardio (Running, Cycling)", "HIIT Workouts", "Jump Rope"],
        "Muscle Gain": ["Weight Lifting", "Bodyweight Exercises", "Progressive Overload"],
        "Flexibility": ["Yoga", "Stretching", "Pilates"],
        "General Fitness": ["Walking", "Swimming", "Light Cardio"]
    }
    return workouts.get(goal, ["No workout suggestions available"])

# Function to suggest diet
def suggest_diet(goal):
    diets = {
        "Weight Loss": ["Lean protein", "Vegetables", "Low-carb diet"],
        "Muscle Gain": ["High protein diet", "Healthy fats", "Complex carbs"],
        "Flexibility": ["Balanced diet", "Hydration", "Anti-inflammatory foods"],
        "General Fitness": ["Fruits", "Nuts", "Whole grains"]
    }
    return diets.get(goal, ["No diet suggestions available"])

# Streamlit UI
st.title("🏋️‍♂️ Fitness & Health Bot")
st.write("Get personalized fitness, workout, and diet recommendations!")

# BMI Calculator
st.header("📊 BMI Calculator")
weight = st.number_input("Enter your weight (kg)", min_value=1.0)
height = st.number_input("Enter your height (m)", min_value=0.5, format="%.2f")

if st.button("Calculate BMI"):
    if weight and height:
        bmi, status = calculate_bmi(weight, height)
        st.success(f"Your BMI is **{bmi:.2f}** ({status})")
    else:
        st.warning("Please enter valid weight and height!")

# Workout & Diet Suggestions
st.header("🏃‍♂️ Fitness & Diet Suggestions")
goal = st.selectbox("Select Your Fitness Goal", ["Weight Loss", "Muscle Gain", "Flexibility", "General Fitness"])

if st.button("Get Recommendations"):
    workouts = suggest_workout(goal)
    diet = suggest_diet(goal)

    st.subheader("🏋️ Workouts")
    for w in workouts:
        st.write(f"- {w}")

    st.subheader("🥗 Diet Recommendations")
    for d in diet:
        st.write(f"- {d}")
