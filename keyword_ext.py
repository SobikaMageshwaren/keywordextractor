import spacy
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# App config
st.set_page_config(page_title="Keyword Extractor", page_icon="🔍", layout="centered")

# Sidebar
st.sidebar.title("⚙️ Settings")
max_keywords = st.sidebar.slider("Number of Keywords", min_value=3, max_value=10, value=5)

# Main Title
st.title("🔑 Intelligent Keyword Extractor")



# Text input area
text = st.text_area("📝 Enter your text here", height=250, placeholder="Paste article, essay, or paragraph here...")

# Function to extract keywords
def extract_keywords(text, top_n=5):
    doc = nlp(text)
    entities = [ent.text for ent in doc.ents]

    if len(entities) < top_n:
        tfidf = TfidfVectorizer(stop_words='english', max_features=top_n)
        tfidf_matrix = tfidf.fit_transform([text])
        feature_names = tfidf.get_feature_names_out()
        entities.extend(feature_names)

    # Remove duplicates while preserving order
    return list(dict.fromkeys(entities))[:top_n]

# Button and processing
if st.button("🚀 Extract Keywords"):
    if not text.strip():
        st.warning("Please enter some text before extracting keywords.")
    else:
        with st.spinner("Extracting keywords..."):
            keywords = extract_keywords(text, max_keywords)
        
        st.success("✅ Keywords extracted successfully!")

        # Show preview
        st.subheader("📄 Text Preview")
        st.write(text[:500] + ("..." if len(text) > 500 else ""))
        st.caption(f"Character count: {len(text)}")

        # Display keywords as tags
        st.subheader("🔍 Top Keywords")
        st.markdown(" ".join([f"`{kw}`" for kw in keywords]))
