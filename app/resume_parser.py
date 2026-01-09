import fitz  # PyMuPDF

def extract_text_from_pdf(file_bytes):
    """
    Extracts text from a PDF resume.
    """
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text.lower()
