from imports.imports import *
watson_url = "https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/2f08faa9-2a55-418b-bcec-002863e2ce9c"
watson_api = "Vg9__qCgmk2U_pZ3YKIFHmOBXiJFzXCsu08WIOwFIGU8"
watson_authenticator = IAMAuthenticator(watson_api)
tts = TextToSpeechV1(authenticator=watson_authenticator)
tts.set_service_url(watson_url)





if "my_chatbot_input" not in st.session_state:
    st.session_state.my_chatbot_input = ""
chatbot_title = st.markdown("<h1 style='text-align: center; color: #ffa31a;'>AI-Chatbot</h1>",
                            unsafe_allow_html=True)
chatbot_input = st.text_input(
    label="User Input", placeholder="Enter your message", value=st.session_state.my_chatbot_input)




if chatbot_input:
    try:
        # user_messages.append(text)
        user_text = st.text("User: "+chatbot_input)
        response = get_response(chatbot_input)
        x = st.info("mssg will be copied to your clipboard automatically")
        time.sleep(3)
        x.empty()
        # bot_replies.append(response)
        bot_text = st.text("Bot: ")
        copy_to_clipboard(response)
        bot_markdown = st.markdown(
            f"""<span style="word-wrap:break-word;">{response}</span>""", unsafe_allow_html=True)
        if os.path.exists("./pages/temp/temp_voices/speech.mp3"):
            os.remove('./pages/temp/temp_voices/speech.mp3')
        if os.path.exists('./pages/temp/temp_voices/speech2.mp3'):
            os.remove('./pages/temp/temp_voices/speech2.mp3')

        with open('./pages/temp/temp_voices/speech.mp3', 'wb') as audio_file:
            res = tts.synthesize(response, accept='audio/mp3',voice='en-US_EmmaExpressive').get_result()
            audio_file.write(res.content)
        st.audio('./pages/temp/temp_voices/speech.mp3')
        st.download_button(label="Download Audio", data='./pages/temp/temp_voices/speech.mp3',file_name='speech.mp3', mime='audio/mp3')
        # with open('./pages/temp/temp_voices/speech2.mp3', 'wb') as audio_file:
        #     res2 = tts.synthesize(response, accept='audio/mp3',
        #                           voice='en-US_MichaelExpressive').get_result()
        #     audio_file.write(res2.content)
        # st.audio('./pages/temp/temp_voices/speech2.mp3')

    except Exception as e:
        error = st.text(e)
