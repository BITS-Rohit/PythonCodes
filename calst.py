# import datetime
#
# import streamlit as st
# from dateutil.relativedelta import relativedelta
#
# """
# Description : We are going to create a Calculator via Streamlit
# Everything is Written on the Web APP
# """
#
# st.title("Calculator")
# st.subheader("By Keshav Gupta")
#
# num1 = st.number_input("First Number")
# num2 = st.number_input("Second Number")
#
# operation = st.radio("Operation", ("Add", "Subs", "Mul", "Divide"))
#
# if operation == "Add":
#     st.success(f"Result : {num1 + num2}")
# elif operation == "Subs":
#     st.success(f"Result : {num1 - num2}")
# elif operation == "Mul":
#     st.success(f"Result : {num1 * num2}")
# elif operation == "Divide":
#     if num2 == 0:
#         st.error("Error: Cannot divide by zero")
#     else:
#         st.success(f"Result : {num1 / num2}")
#
# d = st.date_input(
#     "Pick ur age  date",
#     value=datetime.date.today(),
#     min_value=datetime.date(1900, 1, 1),
#     max_value=datetime.date(2100, 12, 31)
# )
#
# if st.button("Calculate"):
#     today = datetime.date.today()
#     age = relativedelta(today, d)
#     st.write(f"Your Age: {age.years} years, {age.months} months, {age.days} days")
#
# # ed = st.data_editor(num_rows=2)

import sqlite3

import google.generativeai as genai
import streamlit as st


# --------------------
# DATABASE SETUP
# --------------------
def init_db():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS progress
                 (
                     id
                     INTEGER
                     PRIMARY
                     KEY
                     AUTOINCREMENT,
                     name
                     TEXT,
                     year
                     TEXT,
                     lesson
                     TEXT,
                     score
                     INTEGER
                 )""")
    conn.commit()
    return conn


# --------------------
# AI ENGINE (Gemini)
# --------------------
genai.configure(api_key="AIzaSyBp0UzywOYkLEegZQMDtUZR2bHD1Vt-sPY")


def ai_mentor(prompt: str) -> str:
    model = genai.GenerativeModel("gemini-2.5-flash")  # or "gemini-1.5-pro"
    response = model.generate_content(
        f"You are an AI mentor for beginners in Python and AI. {prompt}"
    )
    return response.text


# --------------------
# STREAMLIT UI
# --------------------
st.title("🤖 AI Foundation Mentor")
st.write("Your personal mentor for Python, logic, and AI basics.")

# Student info
name = st.text_input("Enter your name")
year = st.selectbox("Select your year of study", ["1st Year", "2nd Year", "Other"])

# Lesson selection
lesson = st.selectbox("Choose a topic to learn", [
    "Python Basics", "Logic Building", "Math for AI", "Data Handling", "AI Roadmap"
])

if st.button("Get Guidance"):
    with st.spinner("AI Mentor is preparing your lesson..."):
        reply = ai_mentor(f"Teach {lesson} to a {year} student in simple steps with examples.")
        st.success("Here’s your personalized lesson:")
        st.write(reply)

# Quiz section
st.subheader("📘 Quick Quiz")
question = st.text_input("Ask me a practice question on today's topic:")
if st.button("Generate Quiz"):
    quiz = ai_mentor(f"Generate a short quiz (1-2 questions) with answers for {lesson}.")
    st.info(quiz)

# Save progress
if st.button("Save Progress"):
    conn = init_db()
    c = conn.cursor()
    c.execute("INSERT INTO progress (name, year, lesson, score) VALUES (?, ?, ?, ?)",
              (name, year, lesson, 0))
    conn.commit()
    conn.close()
    st.success("Progress saved! 🎉")
