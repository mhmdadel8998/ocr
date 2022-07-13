from PIL import Image
import pytesseract


# Defining paths to tesseract.exe
# and the image we would be using





def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    path_to_tesseract = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
    image_path = filename

    # Opening the image & storing it in an image object
    img = Image.open(image_path)

    # Providing the tesseract executable
    # location to pytesseract library
    pytesseract.tesseract_cmd = path_to_tesseract

    # Passing the image object to image_to_string() function
    # This function will extract the text from the image
    text = pytesseract.image_to_string(img)
    # Displaying the extracted text
   # print(text[:-1])




    # text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

# print(ocr_core('images/ocr_example_1.png'))