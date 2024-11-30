# Hindi and Sanskrit OCR with PDF Processing

This project extracts text from PDF files using Optical Character Recognition (OCR). It is specifically designed to handle **Hindi**, **Sanskrit**, and other Devanagari-based scripts. The project also includes text cleaning, date preservation, and sentence splitting for structured output.

---

## 📜 Features

- Convert PDFs to images using **poppler**.
- Perform OCR on images using **Tesseract**, supporting Hindi (`hin`) and Sanskrit (`san`) language models.
- Clean and preprocess extracted text, preserving dates.
- Split text into sentences based on Devanagari punctuation marks like `।`.
- Save the structured sentences into a `.txt` file for easy access.

---

## 🛠️ Getting Started

### Prerequisites
1. **Python 3.8+**
2. Install the required Python packages:
   ```bash
   pip install pytesseract pdf2image opencv-python-headless numpy
3. Install Tesseract OCR and ensure it is correctly added to your system's PATH.
   ```makefile
   C:\\Program Files\\Tesseract-OCR\\tesseract.exe
4. Install poppler for PDF to image conversion, and add the bin directory to your PATH.

## Folder Structure
   ```bash.
   ├── main.py               # Main script to run the OCR pipeline
   ├── Hiaol_Ramanand_ Jha_Raman.pdf  # Input PDF file
   ├── Hiaol_Ramanand_ Jha_Raman.txt  # Final output text file
   ├── requirements.txt      # Python dependencies
   └── README.md             # Documentation


