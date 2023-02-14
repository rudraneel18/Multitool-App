from imports.imports import * 

if "my_chatbot_input" not in st.session_state:
    st.session_state.my_chatbot_input = ""
chatbot_title = st.markdown("<h1 style='text-align: center; color: #ffa31a;'>Sentiment Analysis</h1>",
                            unsafe_allow_html=True)
chatbot_input = st.text_input(
    label="User Input", placeholder="Enter your message", value=st.session_state.my_chatbot_input)

if chatbot_input:
    try:
        text='Do sentiment analysis of this text "'+chatbot_input+'"'+" and return output in one word"
        response = get_response(text)
        #st.text(response)
        if "negative" in response or "Negative" in response:
            st.error("Negative")
        if "positive" in response or "Positive" in response:
            st.success("Positive")
        if "neutral" in response or "Neutral" in response:
            st.info("Neutral")
        else:
            st.info(response)
    except Exception as e:
        st.error(e)