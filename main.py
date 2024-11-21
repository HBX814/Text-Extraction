import pytesseract
from pdf2image import convert_from_path
import cv2
import numpy as np
import re

# Update this path to point to your Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update with the correct path

# Function to convert PDF to images
def pdf_to_images(pdf_path):
    # Specify the path to the poppler bin directory
    poppler_path = r'C:\Users\harsh\PyCharm_Project\pdf_scraping.py\poppler-24.07.0\Library\bin'  # Update this to your actual poppler bin path
    images = convert_from_path(pdf_path, dpi=150, poppler_path=poppler_path)
    return images

# Function to perform OCR on an image and return extracted text
def ocr_image(image):
    # Convert PIL image to a NumPy array
    image_np = np.array(image)
    # Convert image to RGB
    image_rgb = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)
    # Perform OCR on the image using Hindi or Sanskrit language model
    text = pytesseract.image_to_string(image_rgb, lang='hin')  # or 'san'
    return text

# Function to clean the extracted text
def clean_text(text):
    # Define a regular expression pattern for dates (e.g., dd/mm/yyyy or similar)
    date_pattern = r'\d{1,2}/\d{1,2}(/\d{2,4})?'  # Matches dd, dd/mm, or dd/mm/yyyy

    # Extract dates and preserve them
    dates = re.findall(date_pattern, text)

    # Remove unwanted characters (punctuation, numbers, special characters)
    cleaned_text = re.sub(r'\d[0-9]', '', text)  # Remove all numbers
    cleaned_text = re.sub(r'[“”]', '', cleaned_text)

    # Reinsert the preserved dates back into the cleaned text
    for date in dates:
        cleaned_text = cleaned_text.replace(re.sub(r'\d+', '', date), date)  # Reinsert the preserved dates

    # Remove any extra spaces and trim
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()  # Remove extra spaces and trim

    return cleaned_text

# Function to split text into sentences based on Maithili punctuation
def split_into_sentences(text):
    # Split the text into sentences based on Devanagari punctuation marks used in Maithili
    sentences = re.split(r'(?<=[।!?])\s*', text)
    # Remove any empty sentences and strip whitespace
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    return sentences

# Main function that combines all processes
def main(pdf_path, final_output_path):
    # Step 1: Convert PDF to images
    images = pdf_to_images(pdf_path)
    extracted_text = []

    # Step 2: Perform OCR on each image and accumulate text
    for i, image in enumerate(images):
        text = ocr_image(image)
        extracted_text.append(text)
        print(f'Processed page {i + 1}')

    # Combine all extracted text into a single string
    full_text = '\n'.join(extracted_text)

    # Step 3: Clean the extracted text
    cleaned_text = clean_text(full_text)

    # Step 4: Split the cleaned text into sentences
    sentences = split_into_sentences(cleaned_text)

    # Step 5: Write each sentence to a new line in the final output file
    with open(final_output_path, 'w', encoding='utf-8') as output_file:
        for sentence in sentences:
            output_file.write(sentence + '\n')

    print(f'Text extracted, cleaned, and formatted. Final output saved to {final_output_path}')

# Specify the paths
pdf_path = 'Hiaol_Ramanand_ Jha_Raman.pdf'  # Replace with your PDF file path
final_output_path = 'Hiaol_Ramanand_ Jha_Raman.txt'  # Replace with your desired final output .txt file path

# Run the main function
main(pdf_path, final_output_path)
