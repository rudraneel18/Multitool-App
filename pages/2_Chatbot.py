from imports.imports import *
import uuid

# Set up OpenAI API credentials
openai.api_key = "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"

# Define the GPT-3 model
model_engine = "text-davinci-002"

# Define a function to generate responses using GPT-3


def get_audio_from_text(text):
    try:
        # watson_url = "https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/2f08faa9-2a55-418b-bcec-002863e2ce9c"
        # watson_api = "Vg9__qCgmk2U_pZ3YKIFHmOBXiJFzXCsu08WIOwFIGU8"
        # watson_authenticator = IAMAuthenticator(watson_api)
        # tts = TextToSpeechV1(authenticator=watson_authenticator)
        # tts.set_service_url(watson_url)
        # res=tts.synthesize(text, accept='audio/mp3', voice='en-US_EmmaExpressive').get_result()
        res = gTTS(text=text, lang='en', slow=False)
        path='./pages/temp/temp_voices/speech.mp3'
        res.save(path)
        st.audio(path)
        
    except Exception as e:
        st.error(e)
        return None
    


# Define a function to generate a unique ID for each conversation thread


def generate_thread_id():
    return str(uuid.uuid4())

# Define the main function that runs the chatbot
if 'butt' not in st.session_state:
    st.session_state.butt=0

def run_chatbot():
    st.title("Chatbot")

    # Define a dictionary to store conversation threads
    threads = st.session_state.get("threads", {})

    # Define a "New Thread" button that generates a new thread ID
    if st.button("New Thread"):
        thread_id = generate_thread_id()
        threads[thread_id] = []
        st.session_state.current_thread = thread_id

    # Define a dropdown menu to select a thread
    thread_ids = list(threads.keys())
    if len(thread_ids) > 0:
        thread_id = st.selectbox("Select Thread", thread_ids)
        st.session_state.current_thread = thread_id

    # Get user input and generate a response
    user_input = st.text_input("You", "")
    thread_id = st.session_state.get("current_thread", None)

    if thread_id is not None:
        if user_input:
            if thread_id not in threads:
                threads[thread_id] = []

            threads[thread_id].append(("You", user_input))
            prompt = "\n".join(
                [f"{name}: {message}" for name, message in threads[thread_id]])
            bot_response = get_response(prompt)
            threads[thread_id].append(("Bot", bot_response))

        # Display the conversation thread
        if thread_id in threads:
            for name, message in threads[thread_id]:
                st.markdown(f"{name}: {message}")
                if name=="Bot":
                    if message[:3]=="Bot":
                        get_audio_from_text(message[3:])
                    else:
                        get_audio_from_text(message)

        # Save the conversation thread in session state
        st.session_state.threads = threads


# Run the chatbot
run_chatbot()
