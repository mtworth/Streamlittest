
import streamlit as st 

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

st.markdown("<p style='text-align:right;'><strong>cadence.music</strong></p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:right;'><u><a href='home' target='_self'>home</a></u> | <a href='submit' target='_self'>submit</a> | <a href='archive' target='_self'>archive</a></p>", unsafe_allow_html=True)


st.subheader("archive")

st.markdown("so far, we've sent **91** newsletters and recieved **623** submissions.")

st.markdown("click the images below to browse past newsletters.")
import streamlit as st

# List of image URLs
image_urls = [
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVpv9b3UrfGQOW1g2QTjY4HaNb34GuiGTfbjqWxrJJgQ&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVpv9b3UrfGQOW1g2QTjY4HaNb34GuiGTfbjqWxrJJgQ&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVpv9b3UrfGQOW1g2QTjY4HaNb34GuiGTfbjqWxrJJgQ&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVpv9b3UrfGQOW1g2QTjY4HaNb34GuiGTfbjqWxrJJgQ&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVpv9b3UrfGQOW1g2QTjY4HaNb34GuiGTfbjqWxrJJgQ&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVpv9b3UrfGQOW1g2QTjY4HaNb34GuiGTfbjqWxrJJgQ&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVpv9b3UrfGQOW1g2QTjY4HaNb34GuiGTfbjqWxrJJgQ&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVpv9b3UrfGQOW1g2QTjY4HaNb34GuiGTfbjqWxrJJgQ&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVpv9b3UrfGQOW1g2QTjY4HaNb34GuiGTfbjqWxrJJgQ&s",
]

# Number of columns
num_columns = 3

# Split the image URLs into groups for each column
image_groups = [image_urls[i:i+num_columns] for i in range(0, len(image_urls), num_columns)]

# Create columns dynamically
columns = [st.columns(num_columns) for _ in range(len(image_groups))]

# Iterate through image groups and columns to display images
for image_group, col_group in zip(image_groups, columns):
    for image_url, col in zip(image_group, col_group):
        with col:
            st.markdown("[![Foo](image_url)](http://google.com.au/)")
            st.markdown('#')


