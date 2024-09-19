import requests
from bs4 import BeautifulSoup
import json
import streamlit as st


def scrape_html(url):
    try:
        response = requests.get(url)
        return response.text
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None


def extract_article_segments(html):
    article_title = ""
    article_main_description = []
    article_segments = []
    segment_descriptions = []
    soup = BeautifulSoup(html, 'html.parser')
    
    get_title = soup.find('h1', class_='pulse-title')
    if get_title:
        article_title =  get_title.text.strip()
    
    main_description = soup.find('div', class_='x-article-introduction')
    if main_description:
        span_tag = main_description.find('span', class_='')
        if span_tag:
                article_description = span_tag.text.strip()
                article_main_description.append({
                            "article_description": article_description,
                        })

    containers = soup.find_all('div', class_='article-segment-content-container')
    for container in containers:
        # Case 1: Find h2 tag with empty span
        h2_tag = container.find('h2')
        if h2_tag:
            span_tag = h2_tag.find('span', class_='')
            if span_tag:
                head = span_tag.text.strip()
                
                p_tag = container.find('p')
                if p_tag:
                    span_tag = p_tag.find('span', class_='')
                    if span_tag:
                        description = span_tag.text.strip()
                        
                        article_segments.append({
                            "head": head,
                            "description": description
                        })
                        # Clear segment_descriptions for Case 1
                        segment_descriptions = []
        
        # Case 2: Check if h1 tag is not found and p tag is found
        elif not container.find('h1') and container.find('p'):
            p_tag = container.find('p')
            span_tag = p_tag.find('span')
            if span_tag:
                segment_descriptions.append(span_tag.text.strip())

    return {
        "article_title": article_title,
        "article_main_description": article_main_description,
        "article_segments": article_segments,
        "segment_descriptions": segment_descriptions
    }


def main():
    st.title("LinkedIn Article Scraper")
    url = st.text_input("Enter the LinkedIn article URL:")
    if st.button("Scrape Article"):
        with st.spinner("I am reading the article..."):
            response = extract_article_segments(scrape_html(url))
            if response:
                st.success("Reading completed!")
                st.session_state.response = response
                
    if 'response' in st.session_state:
        response = st.session_state.response
        
        # Display article title
        if response["article_title"]:
            st.subheader(response["article_title"])
        
        # Display article main description
        if response["article_main_description"]:
            st.write(response["article_main_description"][0]["article_description"])
        
        # Display segment descriptions
        if response["segment_descriptions"]:
            st.subheader("You are contributing in")
            st.write(response["segment_descriptions"][0])
        
        # Display article segments
        if response["article_segments"]:
            st.subheader("Select your interest from this article")
            options = [""] + [segment["head"] for segment in response["article_segments"]]
            st.session_state.selected_segment = st.selectbox("Choose segments:", options)
            
            if st.session_state.selected_segment:
                for segment in response["article_segments"]:
                    if segment["head"] == st.session_state.selected_segment:
                        st.subheader(segment["head"])
                        st.write(segment["description"])


if __name__ == "__main__":
    main()