Keyword Extractor
Overview
The Keyword Extractor app intelligently extracts the most relevant keywords from user-provided text. It utilizes spaCy for Named Entity Recognition (NER) and TF-IDF (Term Frequency-Inverse Document Frequency) for extracting meaningful keywords. This tool is designed to help with content analysis, summarization, and improving search engine optimization (SEO).

Features
Extracts keywords from text using spaCy's Named Entity Recognition (NER).

Utilizes TF-IDF for fallback keyword extraction when insufficient entities are found.

Allows the user to specify the number of keywords to extract via a slider.

Displays a preview of the input text and extracted keywords.

Requirements
To run this app locally, you need to have the following Python libraries installed:

streamlit: For creating the web interface.

spacy: For Named Entity Recognition.

sklearn: For TF-IDF keyword extraction.

en_core_web_sm: A small spaCy model for English text processing.

You can install these dependencies using the following commands:

bash
Copy
Edit
pip install streamlit spacy scikit-learn
python -m spacy download en_core_web_sm
How It Works
1. User Input Selection
The user inputs text into the provided text area.

2. Keyword Extraction Using spaCy and TF-IDF
spaCy extracts Named Entities such as names, locations, dates, etc., from the provided text.

If the number of named entities is less than the desired keyword count, TF-IDF is used as a fallback method to extract additional keywords based on frequency and relevance.

3. Combining Keywords
The app combines the extracted entities with the TF-IDF keywords, removing any duplicates and ensuring only the top keywords are retained based on user selection.

4. Displaying Results
The original text is previewed, and the extracted keywords are displayed in a user-friendly format as clickable tags.

User Interface
Text Input: Paste or type the text you want to extract keywords from.

Keyword Count: Use the slider to select the number of keywords you want to extract (default is 5).

Extract Keywords: Click the button to extract keywords and view results.

Example
Enter text (article, essay, or paragraph).

Set the number of keywords (e.g., 5).

Click Extract Keywords.

See the extracted keywords displayed below the input.

Workflow of the Model
User Text Input

The user enters raw text (article, paragraph, etc.) into the provided text area.

Named Entity Recognition (NER) with spaCy

The input text is processed using the spaCy NLP model en_core_web_sm.

Named entities (e.g., names, locations, organizations, dates) are extracted.

TF-IDF Keyword Extraction (Fallback)

If the number of extracted entities is less than the desired keyword count (selected via slider), TF-IDF is applied.

TfidfVectorizer identifies additional keywords based on term frequency and relevance in the input text.

Combining & Filtering Keywords

Extracted entities and TF-IDF keywords are merged and duplicates are removed while preserving order.

The top N keywords (set by the user) are retained.

Output Display

The original text preview is shown (first 500 characters).

The extracted keywords are displayed as styled tags under the "Top Keywords" section.

Future Improvements
Contextual Keyword Extraction: Incorporate deep learning-based keyword extraction models like BERT or GPT to understand context better.

Multiple Language Support: Extend the tool to handle multiple languages using spaCy's multilingual models.

Sentence Segmentation: Enhance the system to extract keywords based on sentence-level significance.

Running the App
Clone this repository or download the code.

Open a terminal and navigate to the directory containing the app.py file.

Run the app with Streamlit:

bash
Copy
Edit
streamlit run app.py
Open your browser and go to the URL displayed in the terminal (usually http://localhost:8501).
