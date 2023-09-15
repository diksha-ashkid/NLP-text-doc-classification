import PyPDF2
import yake

# Function to extract text from a PDF document

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

# Your PDF document path
file_path = r"D:\Personal\diksha\7 SEM\Final Year Project\Marketing Automation (1).pdf"

# Extract text from the PDF document
document_text = extract_text_from_pdf(file_path)

kw_extractor = yake.KeywordExtractor()
keywords = kw_extractor.extract_keywords(document_text)
for kw in keywords:
  print(kw)
