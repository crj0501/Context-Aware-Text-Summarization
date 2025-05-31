import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

class TextExtractor:
    def __init__(self):
        pass

    def extract_text(self, pdf_path):
        full_text = ""

        with fitz.open(pdf_path) as doc:
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                text = page.get_text()

                if text.strip():
                    full_text += text + "\n"
                else:
                    # Perform OCR on image-based pages
                    pix = page.get_pixmap()
                    img_data = pix.tobytes("png")
                    image = Image.open(io.BytesIO(img_data))
                    ocr_text = pytesseract.image_to_string(image)
                    full_text += ocr_text + "\n"

        return full_text
