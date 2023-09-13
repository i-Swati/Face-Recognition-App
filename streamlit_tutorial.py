import streamlit as st

#Text
st.title("This is a title") #print title
st.header("This is a header") #print header
st.subheader("This is a subheader") #print subheader
st.write("Hello World") #print statement

for i in range(3):
    st.write("I am happy")

#Status message Banner
st.success("This is successful") #green
st.warning("This is a warning") #yellow
st.error("This is an error") #red

#Show Images
from PIL import Image
img=Image.open("group.jpg")
st.image(img, width=300, caption="This is a caption")

#upload image/file
img2=st.file_uploader("Upload an image file: ", type=['jpg', 'jpeg','png'])
st.image(img2, width=300, caption="You chose this file.")

#buttons
if st.button("This is a button"):
    st.text("You just clicked a button")

    st.balloons()