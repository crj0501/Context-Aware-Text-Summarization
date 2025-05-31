import re

def clean_text(text):
    """
    Perform basic cleaning of the input text:
    - Remove excessive whitespace
    - Normalize line breaks
    - Remove non-ASCII characters
    """
    text = re.sub(r'\s+', ' ', text)  # Collapse multiple spaces/newlines
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  # Remove non-ASCII chars
    return text.strip()
