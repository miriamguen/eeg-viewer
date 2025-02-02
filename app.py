import streamlit as st
import os

# Set up the page
st.set_page_config(page_title="EEG Viewer", layout="wide")
st.title("EEG Example Viewer")
st.text("For the 7 state analysis in the:\n 'The Hypno-PC: Uncovering Sleep Dynamics through Principal Component Analysis and Hidden Markov Modeling of Electrophysiological Signals.'\n For more detail see: https://biorxiv.org/lookup/doi/10.1101/2025.01.02.631039")

# Display the transition probability figure
svg_file = "transition_prob.svg"
if os.path.exists(svg_file):
    # with open(svg_file, "r") as f:
    #     svg_content = f.read()
    # st.components.v1.html(f'<div style="text-align: center;">{svg_content}</div>', height=800)
    st.image(svg_file, use_container_width=True)
else:
    st.warning("Transition probability figure not found.")

# Define the folder containing EEG images
image_folder = "figures"

# Get a list of available EEG images
images = [img for img in os.listdir(image_folder) if img.endswith(".svg")]

# Extract subjects and states from filenames
subject_names = sorted(set(img.split("_")[0] for img in images))
states = sorted(set(img.split("_")[1].replace('.svg', '') for img in images))

# Create dropdown menus for subject and state
selected_subject = st.selectbox("Select a Subject:", subject_names)
selected_state = st.selectbox("Select a State:", states)

# Find matching image
selected_image = f"{selected_subject}_{selected_state}.svg"
if selected_image in images:
    st.image(os.path.join(image_folder, selected_image), use_container_width=True)
else:
    st.warning("No image available for this selection.")
