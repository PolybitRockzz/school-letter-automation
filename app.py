import streamlit as st
import json
import random

st.title("School Letter Automator 🏫")
st.text("Proffesionalised by Atrayee, F*cked Up by Swastik")

st.header("Your Personal Details")
student_name = st.text_input("Student Name (Eg: John Doe)")
guardian_name = st.text_input("Guardian Name (Eg: Janice Doe)")
student_grade = st.text_input("Student Grade (Eg: 11-A)")

introduction = f"Respected Ma'am,\n\nWe highly respect the decisions made by you and other respected staff of your school for the sole benefit of our ward. However, I'm writing this e-mail to bring light to the genuine problems faced by my ward, {student_name} of  class {student_grade} in attending the Saturday classes:"

ending = f"So, I hereby request you to make these classes available online so, that atleast students, who are willing can attend them.\n\nThanks & Regards,\n{guardian_name}"

st.header("Reasons for not attending Saturday classes")
reasons_json = json.load(open("topics.json", "r"))
reason_1 = st.checkbox(reasons_json[0]["topic"])
reason_2 = st.checkbox(reasons_json[1]["topic"])
reason_3 = st.checkbox(reasons_json[2]["topic"])
reason_4 = st.checkbox(reasons_json[3]["topic"])

action = st.button("Generate Letter")

total_text = ""

notification = st.empty()
result_pane = st.empty()

if action:
    notification = st.empty()
    result_pane = st.empty()

    notification.info("Generating your letter...")

    count = 1
    if reason_1:
        total_text += str(count) + ". " + reasons_json[0]["content"][random.choice([0,1,2])] + "\n\n"
        count += 1
    if reason_2:
        total_text += str(count) + ". " + reasons_json[1]["content"][random.choice([0,1,2])] + "\n\n"
        count += 1
    if reason_3:
        total_text += str(count) + ". " + reasons_json[2]["content"][random.choice([0,1,2])] + "\n\n"
        count += 1
    if reason_4:
        total_text += str(count) + ". " + reasons_json[3]["content"][random.choice([0,1,2])] + "\n\n"
        count += 1

    total_text = introduction + "\n\n" + total_text + ending

    result_pane.text_area("Your Letter", total_text)
    notification.success("Your letter has been generated successfully!")