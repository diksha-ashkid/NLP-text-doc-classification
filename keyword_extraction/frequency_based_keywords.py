
import docx  # For handling .docx files
import PyPDF2  # For handling PDF files
import textract  # For handling various document formats
import re  # For regular expressions
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK data (stopwords and punkt tokenizer models)
nltk.download('stopwords')
nltk.download('punkt')

# Function to extract text from a DOCX file
def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

# Function to extract text from a PDF file
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

# Function to extract text from other document formats (e.g., TXT, RTF)
def extract_text_from_other_formats(file_path):
    text = textract.process(file_path).decode("utf-8")
    return text

# Function to find keywords in text using NLTK
def find_keywords(text, top_n=10):
    # Tokenize the text and remove stopwords
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

    # Create a counter for word frequencies
    word_counter = Counter(filtered_words)

    # Get the top 'top_n' keywords
    top_keywords = word_counter.most_common(top_n)

    return top_keywords

# Main function
def main():
    # Replace 'your_document.docx', 'your_document.pdf', or 'your_document.txt' with the path to your document file.
    file_path = r"C:\Users\DELL\Downloads\Engineer _ Senior Engineer.pdf"

    # Extract text from the document
    if file_path.endswith('.docx'):
        text = extract_text_from_docx(file_path)
    elif file_path.endswith('.pdf'):
        text = extract_text_from_pdf(file_path)
    elif file_path.endswith('.txt') or file_path.endswith('.rtf'):
        text = extract_text_from_other_formats(file_path)
    else:
        print("Unsupported file format")
        return

    # Find keywords using NLTK and display the results
    top_keywords = find_keywords(text)
    print("Top Keywords:")
    for keyword, frequency in top_keywords:
        print(f"{keyword}: {frequency}")

if __name__ == "__main__":
    main()
