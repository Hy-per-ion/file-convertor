from docx2pdf import convert
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def create_empty_pdf(file_path):
    c = canvas.Canvas(file_path, pagesize=letter)
    c.save()


def convert_docx_to_pdf(input_path, output_path):
    try:
        convert(input_path, output_path)
        print("Conversion successful!")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    word_file_path = "word.docx"  # Replace with the path to your Word document
    pdf_file_path = "doc.pdf"  # Replace with the desired output PDF path

    # Create an empty PDF file
    create_empty_pdf(pdf_file_path)

    # Convert the Word file to PDF
    convert_docx_to_pdf(word_file_path, pdf_file_path)
