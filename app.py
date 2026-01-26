import streamlit as st
import random

# Initializing the question bank (I've included a sample of your questions here)
# You can expand this list with the full 70 questions
questions = [
    {
        "q": "Which of the following structures is considered a component of the lower airway?",
        "options": ["Pharynx", "Larynx", "Trachea", "Nasal cavity"],
        "correct": "Trachea",
        "rationale": "The lower airway begins below the larynx and includes the trachea, bronchi, and alveoli."
    },
    # ... (I will provide the full JSON file for you to paste here)
]

st.set_page_config(page_title="EMT ARV Module Review", page_icon="🚑")

st.title("🚑 EMT Airway & Ventilation Practice Test")
st.write("This test pulls 20 random questions from the Fall 2025 Study Guide.")

if 'test_questions' not in st.session_state:
    st.session_state.test_questions = random.sample(questions, min(len(questions), 20))
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.submitted = False

# Progress bar
progress = (st.session_state.current_index) / 20
st.progress(progress)

if st.session_state.current_index < 20:
    item = st.session_state.test_questions[st.session_state.current_index]
    
    st.subheader(f"Question {st.session_state.current_index + 1} of 20")
    st.write(item['q'])
    
    answer = st.radio("Select your answer:", item['options'], index=None)
    
    if st.button("Submit Answer"):
        if answer == item['correct']:
            st.success(f"Correct! 🎯 \n\n {item['rationale']}")
            st.session_state.score += 1
        else:
            st.error(f"Incorrect. The correct answer was: {item['correct']}. \n\n {item['rationale']}")
        
        st.session_state.submitted = True

    if st.session_state.submitted:
        if st.button("Next Question"):
            st.session_state.current_index += 1
            st.session_state.submitted = False
            st.rerun()
else:
    st.balloons()
    st.header("Quiz Complete!")
    st.write(f"Your final score: {st.session_state.score} / 20")
    if st.button("Restart Quiz"):
        del st.session_state.test_questions
        st.rerun()