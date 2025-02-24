# PDF to Text Extractor for Maithili Language

This project is a Python script that extracts text from PDF files, particularly designed for documents in Maithili or other languages using Devanagari script. It uses OCR (Optical Character Recognition) to convert PDF pages to text, cleans the extracted text, and formats it into sentences.

## Features

- Converts PDF files to images
- Performs OCR on images to extract text
- Cleans and formats the extracted text
- Preserves date formats in the text
- Splits the text into sentences based on Devanagari punctuation
- Outputs the processed text to a file

## Requirements

- Python 3.x
- pytesseract
- pdf2image
- opencv-python (cv2)
- numpy
- Tesseract OCR engine
- Poppler

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/HBX814/pdf-to-text-maithili.git
   ```

2. Install the required Python packages:
   ```
   pip install pytesseract pdf2image opencv-python numpy
   ```

3. Install Tesseract OCR engine and ensure it's in your system PATH.

4. Install Poppler and note down the path to its bin directory.

## Usage

1. Update the following paths in the script:
   - Tesseract executable path
   - Poppler bin directory path

2. Run the script with your PDF file:
   ```python
   pdf_path = 'path/to/your/pdf/file.pdf'
   final_output_path = 'path/to/output/text/file.txt'
   main(pdf_path, final_output_path)
   ```

## Functions

- `pdf_to_images(pdf_path)`: Converts PDF to images
- `ocr_image(image)`: Performs OCR on an image
- `clean_text(text)`: Cleans the extracted text
- `split_into_sentences(text)`: Splits text into sentences
- `main(pdf_path, final_output_path)`: Main function that orchestrates the entire process

## Customization

- Adjust the OCR language model in the `ocr_image` function (e.g., 'hin' for Hindi, 'san' for Sanskrit)
- Modify the regular expressions in `clean_text` and `split_into_sentences` functions to suit specific text cleaning needs

## Libraries and Models Used

### pytesseract

Pytesseract is an Optical Character Recognition (OCR) tool for Python, acting as a wrapper for Google's Tesseract OCR Engine. It's used in this project to extract text from images.

Key features:
- Analyzes image structure and layout
- Identifies individual words and characters
- Converts recognized text into a usable format
- Supports multiple languages, including Hindi and Sanskrit

### pdf2image

pdf2image is a Python library that converts PDF files into a sequence of images. It's built on top of the Poppler library, a PDF rendering engine.

Main functionality:
- Converts PDF pages to various image formats (PNG, JPEG)
- Allows for processing PDF content with computer vision algorithms

### OpenCV (cv2)

OpenCV (Open Source Computer Vision Library) is a powerful toolkit for computer vision and machine learning applications.

Key features used in this project:
- Image processing and manipulation
- Color space conversion (BGR to RGB)

### NumPy

NumPy is a fundamental package for scientific computing in Python. In this project, it's used for:

- Handling multidimensional arrays
- Efficient operations on image data

### Tesseract OCR Engine

Tesseract is an open-source OCR engine developed by Google. It's the core technology behind pytesseract and performs the actual text recognition from images.

Key aspects:
- Supports multiple languages and scripts
- Handles various text layouts and fonts
- Continuously improved through machine learning techniques

### Poppler

Poppler is a PDF rendering library used by pdf2image to convert PDF files into images. It's essential for:

- Extracting individual pages from PDF documents
- Converting PDF content to image formats

These libraries and models work together to enable efficient PDF text extraction, particularly for documents in Devanagari script languages like Maithili.

## Contributing

Contributions to improve the script or extend its functionality are welcome. Please feel free to submit a pull request or open an issue.

