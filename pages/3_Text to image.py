from imports.imports import *
st.markdown("<h1 style='text-align: center; color: #ffa31a;'>Text to Image</h1>",
            unsafe_allow_html=True)

st.subheader("Convert text to image")
prompt = st.text_input(label="Your Imagination",
                       placeholder="Enter your text here")

if prompt:
    response = openai.Image.create(prompt=prompt, size="1024x1024")
    columns1 = st.columns(3)
    butcol = st.columns(3)

    with columns1[1]:
        st.write("Original Image")
        image_url = response["data"][0]["url"]
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img.save("./pages/temp/temp_images/temp_image.png")
        loaded_img = Image.open("./pages/temp/temp_images/temp_image.png")
        loaded_img = loaded_img.resize((400, 400))
        st.image(img, caption=prompt)
        st.write("Variation of Image")
        response = openai.Image.create_variation(image=open(
            "./pages/temp/temp_images/temp_image.png", "rb"), n=5, size="1024x1024")
        for i in range(5):
            image_url = response["data"][i]["url"]
            response = requests.get(image_url)
            rimg = Image.open(BytesIO(response.content))
            rimg.save(f'./pages/temp/temp_images/temp_image_{i}.png')
            rimg = rimg.resize((400, 400))
            st.image(rimg, caption=prompt+" variation")
        st.grid_container(children=[st.image(
            f'./pages/temp/temp_images/temp_image_{i}.png', width=200) for i in range(5)], width=800)
