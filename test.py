try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string
print(pytesseract.image_to_string(Image.open(r'C:\Users\param\Documents\GitHub\OCR\web-banner_covid-test-online-booking.png')))
print(pytesseract.image_to_string(Image.open(r'C:\Users\param\Documents\GitHub\OCR\testIO-logo-rgb-2.png')))

# Get bounding box estimates
print(pytesseract.image_to_boxes(Image.open(r'C:\Users\param\Documents\GitHub\OCR\testIO-logo-rgb-2.png')))
