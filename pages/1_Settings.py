# app.py

import streamlit as st
import toml
import os

# Define the path to your config.toml
CONFIG_PATH = '.streamlit/config.toml'

# Function to load the current configuration
def load_config(path):
    if not os.path.exists(path):
        # If config.toml doesn't exist, create it with default values
        default_config = {
            "theme": {
                "primaryColor": "#FFDC1E",
                "backgroundColor": "#0F1116",
                "secondaryBackgroundColor": "#14161B",
                "textColor": "#F8F8F8",
                "font": "sans serif"
            }
        }
        with open(path, 'w') as f:
            toml.dump(default_config, f)
        return default_config
    else:
        with open(path, 'r') as f:
            return toml.load(f)

# Function to save the updated configuration
def save_config(path, config):
    with open(path, 'w') as f:
        toml.dump(config, f)

# Load existing config
config = load_config(CONFIG_PATH)

st.title("Theme Customizer")

# Create columns for layout
cols1, cols2, cols3 = st.columns([1, 1, 1])

with cols1:
    st.subheader("Primary Color")
    primary_color = st.color_picker("Select Primary Color", config['theme']['primaryColor'])

with cols2:
    st.subheader("Background Color")
    background_color = st.color_picker("Select Background Color", config['theme']['backgroundColor'])

with cols3:
    st.subheader("Secondary Background Color")
    secondary_background_color = st.color_picker("Select Secondary Background Color", config['theme']['secondaryBackgroundColor'])

# Additional theme settings
st.subheader("Text Color")
text_color = st.color_picker("Select Text Color", config['theme']['textColor'])

st.subheader("Font")
font = st.selectbox("Choose Font", ["sans serif", "serif", "monospace"], index=["sans serif", "serif", "monospace"].index(config['theme']['font']))

# Save Button
if st.button("Save Configuration"):
    # Update the config dictionary with new values
    config['theme']['primaryColor'] = primary_color
    config['theme']['backgroundColor'] = background_color
    config['theme']['secondaryBackgroundColor'] = secondary_background_color
    config['theme']['textColor'] = text_color
    config['theme']['font'] = font
    
    # Save the updated config to config.toml
    save_config(CONFIG_PATH, config)
    
    st.success("Configuration saved successfully!")