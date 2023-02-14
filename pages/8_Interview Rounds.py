from imports.imports import *
model_engine = "text-davinci-002"


def generate_questions(category, skills, profile):
    if category == "HR":
        prompt = f"Generate 1 HR interview question for {profile} profile based on the following skills: {skills}"
    elif category == "Technical":
        prompt = f"Generate 1 technical interview question for {profile} profile based on the following skills: {skills}"
    else:
        return "Invalid category"

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message


def analyze_answer(transcribed_data, question, category):
    prompt = f"Evaluate the following answer for the question as a {category} interviewer and state the points to improve by giving feedback to my answer: Question- {question} Answer- {transcribed_data} "

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message


def better_answer(question, category):
    prompt = f"Evaluate the following question as a {category} interviewer and tell me what should be the correct answer from an interviewee. Make it sound like a human would converse. Question- {question} also give me the best answer possible in 4 to 5 paragraphs"

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message


def get_important_skills(job_description):
    prompt = f"What are the most important skills for the following job description: {job_description}"

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message


def main():
    st.title("Interview Question Generator")

    job_description = st.text_input(
        "Enter the job description here ending with a slash and job profile (..... /Data Scientist)")
    profile = job_description.split("/")[-1]
    job_description = job_description.split("/")[0]
    send_button = st.checkbox("Send")
    if 'skills' not in st.session_state:
        st.session_state.skills = ""
    if 'regen_ques_button' not in st.session_state:
        st.session_state.regen_ques_button = False
    if send_button and job_description:
        if st.session_state.skills == "":
            skills = get_important_skills(job_description)
            st.session_state['skills'] = skills
        st.write("Important Skills: ", st.session_state.skills)

        category = st.selectbox(
            "Select the category of interview questions", ["HR", "Technical"])
        generate_q = st.checkbox("generate question")
        if 'generated_ques' not in st.session_state:
            st.session_state.generated_ques = ""
        if generate_q:
            if st.session_state.generated_ques == "" and st.session_state.regen_ques_button == False:
                question = generate_questions(category, st.session_state.skills, profile)
                st.session_state.generated_ques = question
            print_ques=st.write("Previous Generated Question: ", st.session_state.generated_ques)

            def regenerate1(print_ques):
                st.session_state.regen_ques_button = False
                print_ques = st.empty()
                question = generate_questions(
                    category, st.session_state.skills, profile)
                st.session_state.generated_ques = question
                print_ques = st.write(
                    "Current Generated Question: ", st.session_state.generated_ques)
            
            regenerate=st.button("regenerate question",on_click=regenerate1(print_ques))
            
            transcribed_data = st.text_input(
                "Enter the transcribed data of the interviewee's answer")
            submit = st.checkbox("submit")
            if transcribed_data and submit:
                feedback = analyze_answer(
                    transcribed_data, st.session_state.generated_ques, category)
                st.write("Feedback: ", feedback)
                expected_answer = better_answer(
                    question=st.session_state.generated_ques, category=category)
                st.write(f"Expected answer{expected_answer}")


if __name__ == '__main__':
    main()
