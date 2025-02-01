import streamlit as st
import os

# Set up the page
st.set_page_config(page_title="EEG Viewer", layout="wide")
st.title("EEG Example Viewer")

# Display the transition probability figure
svg_file = "transition_prob.svg"
if os.path.exists(svg_file):
    st.markdown(f'<div style="text-align: center;"><img src="{svg_file}" width="80%"></div>', unsafe_allow_html=True)
else:
    st.warning("Transition probability figure not found.")

# Define the folder containing EEG images
image_folder = "figures"

# Get a list of available EEG images
images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

# Extract subjects and states from filenames
subject_names = sorted(set(img.split("_")[0] for img in images))
states = sorted(set(img.split("_")[1] for img in images))

# Create dropdown menus for subject and state
selected_subject = st.selectbox("Select a Subject:", subject_names)
selected_state = st.selectbox("Select a State:", states)

# Find matching image
selected_image = f"{selected_subject}_{selected_state}_.png"
if selected_image in images:
    st.image(os.path.join(image_folder, selected_image), use_container_width=True)
else:
    st.warning("No image available for this selection.")
