import streamlit as st
import pytesseract
from PIL import Image
import pdfplumber
import os
import requests
from gtts import gTTS
import tempfile
import time

# ✅ Page Configuration (MUST BE FIRST STREAMLIT COMMAND)
st.set_page_config(page_title="PDF/Image to Speech", page_icon="📖", layout="wide")

# ✅ Set up tessdata directory and download models if missing
TESSDATA_DIR = "tessdata"
TESSDATA_URL = "https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO/raw/main/tessdata"  # UPDATE THIS URL

if not os.path.exists(TESSDATA_DIR):
    os.makedirs(TESSDATA_DIR)

models = ["eng.traineddata", "hin.traineddata", "tel.traineddata"]

for model in models:
    model_path = os.path.join(TESSDATA_DIR, model)
    if not os.path.exists(model_path):
        url = f"{TESSDATA_URL}/{model}"
        with open(model_path, "wb") as f:
            f.write(requests.get(url).content)

os.environ["TESSDATA_PREFIX"] = TESSDATA_DIR  # ✅ Ensure Tesseract finds models

# ✅ Install Tesseract in Streamlit Cloud
def install_tesseract():
    if not os.path.exists("/usr/bin/tesseract"):
        st.warning("Installing Tesseract OCR...")
        os.system("sudo apt-get update && sudo apt-get install -y tesseract-ocr")

install_tesseract()

# ✅ Set Tesseract OCR Path
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

# Sidebar Title
with st.sidebar:
    st.title("📖 Text to Speech")
    st.markdown("Convert **PDFs & Images** into natural-sounding speech.")
    st.markdown("---")
    st.markdown("**✨ Features:**")
    st.write("✅ Extract text from PDFs & Images")
    st.write("✅ Multilingual Support (Telugu, Hindi, English)")
    st.write("✅ Play and Download Speech")
    st.write("✅ Stylish UI with Animations")
    
    st.caption("Developed with ❤️ using **Streamlit**")
    st.sidebar.write("### About the Developer")
    st.sidebar.write("**Bipin Gundala**")
    st.sidebar.write("I am a software developer with a passion for building machine learning applications.")
    st.sidebar.write("This project is aimed at helping farmers identify plant diseases using deep learning.")
    st.sidebar.write("**Contact Information:**")
    st.sidebar.write("- **Email:** bipin.gundala@gmail.com")
    st.sidebar.write("- **LinkedIn:** [LinkedIn Profile](https://www.linkedin.com/in/bipin-gundala-b54496210/)")

# Title with Animation
st.markdown("<h1 style='text-align: center;'>📄 PDF/Image to Speech Converter</h1>", unsafe_allow_html=True)

# Function to extract text from an image
def extract_text_from_image(image):
    return pytesseract.image_to_string(image, lang="eng+hin+tel")

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()

# Function to convert text to speech using gTTS
def speak_text(text, lang="te"):  # Default language is Telugu ("te")
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp_audio.name)
        return temp_audio.name
    except Exception as e:
        st.error(f"❌ Error in text-to-speech conversion: {e}")
        return None

# File Upload Section
uploaded_file = st.file_uploader("📤 Upload an Image or PDF", type=["png", "jpg", "jpeg", "pdf"])

if uploaded_file is not None:
    file_extension = os.path.splitext(uploaded_file.name)[-1].lower()

    extracted_text = ""
    if file_extension in [".png", ".jpg", ".jpeg"]:
        image = Image.open(uploaded_file)
        st.image(image, caption="🖼 Uploaded Image", use_column_width=True)
        with st.spinner("🔍 Extracting text from image..."):
            time.sleep(2)
            extracted_text = extract_text_from_image(image)
    
    elif file_extension == ".pdf":
        with st.spinner("📄 Extracting text from PDF..."):
            time.sleep(2)
            extracted_text = extract_text_from_pdf(uploaded_file)

    else:
        st.error("❌ Unsupported file format!")

 
    if extracted_text:
        st.subheader("📜 Extracted Text:")
        st.text_area("📝 Text", extracted_text, height=200)  # ✅ Fixed syntax error

    # Language selection
        lang_choice = st.selectbox("🌍 Choose Language for Speech:", ["Telugu (te)", "Hindi (hi)", "English (en)"])
        lang_code = {"Telugu (te)": "te", "Hindi (hi)": "hi", "English (en)": "en"}[lang_choice]

    # Read aloud button
        if st.button("🔊 Read Aloud", use_container_width=True):
            with st.spinner("🔉 Generating speech..."):
                time.sleep(2)
                audio_path = speak_text(extracted_text, lang=lang_code)
                if audio_path:
                    st.success("✅ Speech generated successfully!")
                    st.audio(audio_path, format="audio/mp3")
                    st.download_button("⬇ Download Audio", data=open(audio_path, "rb"), file_name="speech.mp3", mime="audio/mp3")


