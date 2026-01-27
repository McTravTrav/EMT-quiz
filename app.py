import streamlit as st
import random

# --- 1. THE FULL 70-QUESTION MASTER BANK ---
# Ensure you have your full list of 70 questions here.
MASTER_QUESTIONS = [
    {"q": "Which structure is the dividing line between the upper and lower airway?", "options": ["Pharynx", "Larynx", "Trachea", "Carina"], "correct": "Larynx", "rationale": "The larynx (specifically the vocal cords) is the transition point between upper and lower airways."},
    {"q": "What is the primary stimulus for breathing in a healthy patient?", "options": ["Low O2 levels", "High CO2 levels", "Blood pH", "High O2 levels"], "correct": "High CO2 levels", "rationale": "Healthy people breathe based on CO2 levels in the blood/CSF (Hypercarbic Drive)."},
    {"q": "Which nerve innervates the diaphragm?", "options": ["Vagus nerve", "Phrenic nerve", "Sciatic nerve", "Intercostal nerve"], "correct": "Phrenic nerve", "rationale": "The phrenic nerve (C3-C5) controls the diaphragm. Remember: 'C3, 4, 5 keep the diaphragm alive.'"},
    {"q": "Where does gas exchange specifically occur in the lungs?", "options": ["Bronchioles", "Trachea", "Alveoli", "Pleura"], "correct": "Alveoli", "rationale": "Gas exchange occurs at the alveolar-capillary membrane via diffusion."},
    {"q": "What is the function of the epiglottis?", "options": ["Speech production", "Protecting the airway during swallowing", "Triggering coughs", "Filtering air"], "correct": "Protecting the airway during swallowing", "rationale": "It is a leaf-shaped cartilage that covers the glottic opening to prevent aspiration."},
    {"q": "Minute Volume is calculated as:", "options": ["TV + RR", "TV x RR", "TV / RR", "RR - TV"], "correct": "TV x RR", "rationale": "Minute Volume = Tidal Volume multiplied by Respiratory Rate."},
    {"q": "What is 'Dead Space' in the respiratory system?", "options": ["Air that doesn't reach the alveoli", "Air left after max exhalation", "Air in a pneumothorax", "Air inside a BVM"], "correct": "Air that doesn't reach the alveoli", "rationale": "Dead space is air in the trachea/bronchi where no gas exchange occurs."},
    {"q": "A high-pitched, whistling sound heard on inhalation is called:", "options": ["Wheezing", "Rales", "Stridor", "Rhonchi"], "correct": "Stridor", "rationale": "Stridor indicates a partial upper airway obstruction."},
    {"q": "A 'Gurgling' sound in the airway indicates:", "options": ["Tongue obstruction", "Fluid in the airway", "Bronchoconstriction", "Normal breathing"], "correct": "Fluid in the airway", "rationale": "Gurgling is air moving through liquid; it is an immediate indication for suctioning."},
    {"q": "What is the maximum suction time for an adult patient?", "options": ["5 seconds", "10 seconds", "15 seconds", "30 seconds"], "correct": "15 seconds", "rationale": "Suctioning removes oxygen; limiting to 15 seconds prevents severe hypoxia."},
    {"q": "The 'O' in DOPE stands for:", "options": ["Oxygen", "Obstruction", "Output", "Over-ventilation"], "correct": "Obstruction", "rationale": "Obstruction (like a mucus plug) is a common failure in tracheostomies."},
    {"q": "What is the primary effect of CPAP?", "options": ["Decrease RR", "Opening collapsed alveoli", "Suctioning mucus", "Increasing pulse"], "correct": "Opening collapsed alveoli", "rationale": "CPAP uses pressure to keep alveoli open at the end of exhalation."},
    # ... [MAKE SURE TO PASTE ALL 70 QUESTIONS INTO THIS LIST] ...
]

# --- 2. THE SMART SHUFFLE ENGINE ---
def initialize_quiz():
    full_list = list(MASTER_QUESTIONS)
    random.shuffle(full_list)
    st.session_state.master_pool = full_list
    st.session_state.current_test = full_list[:20]
    st.session_state.remaining_pool = full_list[20:]
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.show_review = False
    st.session_state.missed_questions = [] # Track wrong answers

if 'master_pool' not in st.session_state:
    initialize_quiz()

# --- 3. UI LAYOUT ---
st.set_page_config(page_title="EMT ARV Master Review", page_icon="🚑")
st.title("🚑 EMT ARV Master Review")
st.sidebar.header("Progress Tracker")
st.sidebar.write(f"Questions left in bank: **{len(st.session_state.remaining_pool)}**")
st.sidebar.write(f"Questions missed so far: **{len(st.session_state.missed_questions)}**")

idx = st.session_state.current_index
total = len(st.session_state.current_test)

if idx < total:
    st.progress(idx / total)
    q_item = st.session_state.current_test[idx]
    
    st.subheader(f"Question {idx + 1} of {total}")
    st.markdown(f"### {q_item['q']}")
    
    user_choice = st.radio("Select the correct answer:", q_item['options'], index=None, key=f"q_{idx}")

    if not st.session_state.get('show_review', False):
        if st.button("Submit Answer"):
            if user_choice:
                st.session_state.show_review = True
                st.rerun()
            else:
                st.warning("Please select an option.")
    else:
        if user_choice == q_item['correct']:
            st.success("**Correct!**")
        else:
            st.error(f"**Incorrect.** The correct answer was: {q_item['correct']}")
            # Add to missed list if it's not already there
            if q_item not in st.session_state.missed_questions:
                st.session_state.missed_questions.append(q_item)
        
        st.info(f"**Rationale:** {q_item['rationale']}")
        
        if st.button("Next Question →"):
            if user_choice == q_item['correct']:
                st.session_state.score += 1
            st.session_state.current_index += 1
            st.session_state.show_review = False
            st.rerun()

else:
    # --- END OF SET LOGIC ---
    st.balloons()
    st.header("🏁 Set Complete!")
    st.metric("Set Score", f"{st.session_state.score} / {total}")
    
    # Show missed questions for review
    if st.session_state.missed_questions:
        with st.expander("📝 Review Your Missed Questions"):
            for m in st.session_state.missed_questions:
                st.write(f"**Q:** {m['q']}")
                st.write(f"**Correct Answer:** {m['correct']}")
                st.write(f"**Rationale:** {m['rationale']}")
                st.write("---")

    if len(st.session_state.remaining_pool) > 0:
        next_batch_size = min(len(st.session_state.remaining_pool), 20)
        if st.button(f"Start Next {next_batch_size} Unique Questions"):
            new_pool = st.session_state.remaining_pool
            st.session_state.current_test = new_pool[:next_batch_size]
            st.session_state.remaining_pool = new_pool[next_batch_size:]
            st.session_state.current_index = 0
            st.session_state.score = 0
            st.session_state.show_review = False
            st.rerun()
    else:
        st.success("You have completed the entire question bank!")
        if st.button("Reshuffle and Restart Everything"):
            initialize_quiz()
            st.rerun()