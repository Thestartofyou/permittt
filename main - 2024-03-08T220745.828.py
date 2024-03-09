import cv2
import pytesseract

def extract_text_from_image(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform OCR using Tesseract
    extracted_text = pytesseract.image_to_string(gray_image)

    return extracted_text

def main():
    # Path to the image file
    image_path = 'permit_image.jpg'

    # Extract text from the image
    extracted_text = extract_text_from_image(image_path)

    # Organize the extracted data (For demonstration, simply printing the text)
    print("Extracted Text:")
    print(extracted_text)

if __name__ == "__main__":
    main()
