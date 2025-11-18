import streamlit as st
import requests

st.set_page_config(page_title="Web2Desktop Online", layout="centered")

st.title("🌐 Web2Desktop")
st.caption("Turn any website into a fullscreen web app")

# Input fields
app_name = st.text_input("App Name", placeholder="My Cool App")
url = st.text_input("Website URL", placeholder="https://example.com")

# Launch button
if st.button("Launch App"):
    if not app_name or not url:
        st.warning("Please enter both an app name and a URL.")
    else:
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.head(url, headers=headers, allow_redirects=True, timeout=5)
            x_frame = response.headers.get("X-Frame-Options", "").lower()

            if "deny" in x_frame or "sameorigin" in x_frame:
                st.error("🚫 This site blocks embedding in other apps.")
                st.markdown(f"🔗 [Click here to open **{app_name}** in a new tab]({url})", unsafe_allow_html=True)
            else:
                st.success(f"🚀 Launching **{app_name}** below!")
                st.components.v1.iframe(url, height=800, scrolling=True)
        except requests.exceptions.RequestException:
            st.error("⚠️ Could not connect to the site. Please check the URL.")