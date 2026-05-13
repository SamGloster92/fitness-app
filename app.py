import streamlit as st
import pandas as pd
from datetime import date
import os

# --- 1. SET UP THE PAGE ---
st.set_page_config(page_title="Skinny-Fat Slayer", page_icon="💪", layout="centered")

# --- 2. DATA STORAGE SETUP ---
# Updated to track weight in kg
DATA_FILE = "workout_log.csv"
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["Date", "Workout Day", "Backpack Weight (kg)", "Notes"])
    df.to_csv(DATA_FILE, index=False)

# --- 3. SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to:", ["🏋️ Tracker", "📚 The Vault", "🥩 Nutrition"])

# --- 4. TAB 1: TRACKER ---
if menu == "🏋️ Tracker":
    st.header("The Skinny-Fat Slayer Tracker")
    st.write("Log your progress and track your progressive overload. Get it done, then get back to your family.")
    
    # Input Fields
    workout_day = st.selectbox("Which day did you complete?", ["Monday (Upper Body Width)", "Wednesday (Legs & Core)", "Friday (Full Body Burn)"])
    
    # Updated: Changed lbs to kg, adjusted max value to a realistic kg amount
    weight = st.number_input("Backpack Weight used (kg):", min_value=0, max_value=70, value=5, step=1)
    notes = st.text_area("Notes (e.g., Hit 12 reps on push-ups!):")
    
    # Save Button
    if st.button("Log Workout"):
        new_data = pd.DataFrame({
            "Date": [date.today().strftime("%Y-%m-%d")],
            "Workout Day": [workout_day],
            "Backpack Weight (kg)": [weight],
            "Notes": [notes]
        })
        new_data.to_csv(DATA_FILE, mode='a', header=False, index=False)
        st.success("Workout logged successfully! Great job today.")
        
    st.divider()
    
    # History Log
    st.subheader("Your Progress History")
    history_df = pd.read_csv(DATA_FILE)
    if not history_df.empty:
        st.dataframe(history_df, use_container_width=True, hide_index=True)
    else:
        st.info("No workouts logged yet. Start today!")

# --- 5. TAB 2: THE VAULT ---
elif menu == "📚 The Vault":
    st.header("Exercise Vault & Form Cues")
    st.write("Remember: Control the muscle. Tension and effort matter more than speed.")
    
    with st.expander("Push-ups & Pike Push-ups (Monday / Friday)"):
        st.write("""
        * **Standard Push-up:** Hands slightly wider than shoulder-width. Keep your core tight like a plank. Drop to your knees if your form breaks down.
        * **Pike Push-up:** Body in an inverted 'V' shape. Lower the top of your head to the floor to target the shoulders.
        """)
        
    with st.expander("Backpack Rows (Monday)"):
        st.write("""
        * **Form:** Hinge at the hips, back flat, almost parallel to the floor. 
        * **Cue:** Pull the backpack to your belly button, squeezing your shoulder blades together to fix that desk posture.
        """)
        
    with st.expander("Bulgarian Split Squats (Wednesday)"):
        st.write("""
        * **Form:** One foot elevated behind you on a sturdy chair. Lower straight down.
        * **Cue:** Keep your chest up. These are uncomfortable, but they are essential for fixing skinny-fat proportions.
        """)
        
    with st.expander("Backpack Deadlifts (Friday)"):
        st.write("""
        * **Form:** Hinge at the hips, slight bend in the knees. Keep the backpack close to your legs.
        * **Cue:** Push your hips backward like you're trying to shut a car door with your glutes.
        """)

# --- 6. TAB 3: NUTRITION ---
elif menu == "🥩 Nutrition":
    st.header("Protein Target Calculator")
    st.write("Rule #4: 80% consistency is better than a miserable 100% perfect diet.")
    
    # Updated: Using kilograms for the bodyweight slider
    body_weight = st.slider("What is your current body weight (kg)?", min_value=40, max_value=140, value=75)
    
    # Updated: Metric protein math (1.6g to 2.2g per kg of body weight for muscle building)
    min_protein = int(body_weight * 1.6)
    max_protein = int(body_weight * 2.2)
    
    st.subheader(f"🎯 Daily Goal: {min_protein}g - {max_protein}g of Protein")
    st.write("If you eat 3 meals a day, aim for roughly **{}g per meal**.".format(int(min_protein/3)))
    
    st.write("---")
    st.write("**Top Tips:**")
    st.write("1. **Stop drinking liquid calories** (sodas, sugary coffees).")
    st.write("2. **Do not starve yourself.** It burns the muscle you are trying to build.")
    st.write("3. **Easy Protein:** Eggs, lean meats, and plain Greek yogurt.")
