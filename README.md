📄 PDF/Image to Speech Converter
📝 Overview
This is a Streamlit-based web application that extracts text from PDFs and images (JPG, PNG) and converts it into speech using Google Text-to-Speech (gTTS). It supports English, Hindi, and Telugu languages.

🚀 Features
✅ Extract text from PDFs & Images
✅ Supports Telugu, Hindi, and English
✅ Listen to extracted text using gTTS
✅ Download the generated speech as an audio file
✅ Simple UI with a sidebar and animations

🛠 Installation
Step 1: Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/pdf-to-speech.git
cd pdf-to-speech
Step 2: Install Dependencies
Make sure you have Python 3.8+ installed. Then, run:

bash
Copy
Edit
pip install -r requirements.txt
Step 3: Install Tesseract OCR
Download and install Tesseract from: Tesseract-OCR
After installation, update the pytesseract path in app.py:

python
Copy
Edit
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
▶ How to Run
Start the Streamlit application:

bash
Copy
Edit
streamlit run app.py
Then, open the local URL in your browser.

📌 Usage
1️⃣ Upload a PDF or Image
2️⃣ Extract text from the uploaded file
3️⃣ Click "🔊 Convert to Speech" to listen
4️⃣ Click "⬇ Download Audio" to save the speech file

🌍 Supported Languages
English (en)
Hindi (hi)
Telugu (te)
🔧 Troubleshooting
Error: Tesseract Not Found?
➝ Make sure Tesseract-OCR is installed and update the path in app.py.
Speech Not Working?
➝ Ensure gtts is installed properly using pip install gtts.
💡 Future Enhancements
🔹 Support for more languages
🔹 Customizable voice and speed settings
🔹 Deploy online for public access

👨‍💻 About the Developer
Developed by Bipin Gundala
📧 Email: bipin.gundala@gmail.com
🔗 LinkedIn Profile

📝 License
This project is open-source and available under the MIT License.