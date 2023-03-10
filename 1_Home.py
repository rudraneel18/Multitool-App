from imports.imports import *
openai_api_key = "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"
openai.api_key = openai_api_key


st.set_page_config(page_title="Chatbot and Text to Image",
                   page_icon="logo.png", layout="wide", initial_sidebar_state="expanded")
st.title("Welcome to my Multitool App")
st.warning("created by Rudraneel Dutta")
# tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
# tab1.write  ("this is tab 1")
# tab2.write("this is tab 2")
