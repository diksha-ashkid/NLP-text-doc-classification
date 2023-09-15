import PyPDF2
import docx
import yake
import os

def extract_text_from_document(file_path):
    file_extension = os.path.splitext(file_path)[-1].lower()
    text = ""

    if file_extension == '.pdf':
        # Extract text from a PDF document
        with open(file_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                text += pdf_reader.pages[page_num].extract_text()
    


    elif file_extension == '.docx':
        # Extract text from a Word document
        doc = docx.Document(file_path)
        for paragraph in doc.paragraphs:
            text += paragraph.text + '\n'

    elif file_extension == '.txt':
        # Read text from a plain text document
        with open(file_path, 'r', encoding='utf-8') as text_file:
            text = text_file.read()

    else:
        print("Unsupported file type. Supported types: PDF, DOCX, TXT")

    return text

# Usage example:
file_path = r"doc_to_read.pdf"
document_text = extract_text_from_document(file_path)

kw_extractor = yake.KeywordExtractor()
keywords = kw_extractor.extract_keywords(document_text)
for kw in keywords:
    print(kw)
