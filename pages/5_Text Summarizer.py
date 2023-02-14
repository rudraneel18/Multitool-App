from imports.imports import * 

if "my_chatbot_input" not in st.session_state:
    st.session_state.my_chatbot_input = ""
chatbot_title = st.markdown("<h1 style='text-align: center; color: #ffa31a;'>Text Summarizer</h1>",
                            unsafe_allow_html=True)
chatbot_input = st.text_input(
    label="User Input", placeholder="Enter your message", value=st.session_state.my_chatbot_input)
xinput=st.text_input(label="enter number of words you want",value="50")
if chatbot_input:
    if xinput:
        try:
            text='Summarize this text "'+chatbot_input+'"'+f' in {xinput} words'
            response = get_response(text)
            copy_to_clipboard(response)
            st.markdown("<h3 style='text-align: center; color: #ffffff; font-size: 50px;'>Summary</h3>", unsafe_allow_html=True)
            display_response=st.markdown(f"<h3 style='text-align: left; color: #ffa31a;'>{response}</h3>", unsafe_allow_html=True)
        except Exception as e:
            st.warning(e)