from pdf2docx import parse
from typing import Tuple


def convert_pdf2docx(in_file: str, out_file: str, pages: Tuple = None):
    if pages:
        pages = [int(i) for i in list(pages) if i.isnumeric()]
    result = parse(pdf_file=in_file,
                   docx_with_path=out_file, pages=pages)
    summary = {
        "File": in_file, "Pages": str(pages), "Output File": out_file
    }
    print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
    return result


if __name__ == "__main__":
    input_file = input("Enter the pdf path: ")
    output_file = input("Enter the docx path: ")
    convert_pdf2docx(input_file, output_file)
