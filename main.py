import streamlit as st
import requests
import json

st.title("URL Shortener & Unshortener")

# Tabs for navigation
tab1, tab2 = st.tabs(["Shorten URL", "Unshorten URL"])

with tab1:
    st.header("Shorten a URL")
    url_to_shorten = st.text_input("Enter the URL to shorten:", placeholder="https://www.example.com")
    custom_short_url = st.text_input("Optional: Enter a custom short URL (leave blank for default):",
                                     placeholder="example")

    if st.button("Shorten URL"):
        api_url = "https://is.gd/create.php"
        params = {
            "format": "simple",
            "url": url_to_shorten,
        }

        if custom_short_url:
            params["shorturl"] = custom_short_url

        try:
            response = requests.get(api_url, params=params)
            response.raise_for_status()

            shortened_url = response.text
            st.success(f"Shortened URL: {shortened_url}")

        except requests.exceptions.RequestException as e:
            st.error(f"Error: {str(e)}")

with tab2:
    st.header("Unshorten a URL")
    url_to_unshorten = st.text_input("Enter the shortened URL to unshorten:", placeholder="https://bit.ly/3DKwm5t")

    if st.button("Unshorten URL"):
        api_url = "https://unshorten.me/api/v2/unshorten"
        headers = {
            "Authorization": "Token 6b294d034fc63516b8da4912532effd35597c"
        }
        params = {
            "url": url_to_unshorten
        }

        try:
            response = requests.get(api_url, headers=headers, params=params)
            response.raise_for_status()

            data = response.json()
            st.success(f"Original URL: {json.dumps(data, indent=4)}")

        except requests.exceptions.RequestException as e:
            st.error(f"Error: {str(e)}")

st.write("Powered by is.gd and unshorten.me services")