import fitz
import os

def load_pdf(pdf_path):
    document = fitz.open(pdf_path)

    pages =[]

    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text = page.get_text()
        pages.append({
            "source": os.path.basename(pdf_path),
            "page": page_num + 1,
            "text": text
        })

    return pages

def load_all_pdfs(data_folder):
    all_pages = []

    for file_name in os.listdir(data_folder):

        if file_name.endswith(".pdf"):

            pdf_path = os.path.join(data_folder, file_name)

            pages = load_pdf(pdf_path)

            all_pages.extend(pages)

    return all_pages

