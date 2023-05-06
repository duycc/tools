from pypdf import PdfMerger
import os


def merge_pdf():
    base_path = "/Users/duyong/Desktop/"
    pdf_files = [f for f in os.listdir(base_path) if f.endswith(".pdf")]
    pdf_files = [os.path.join(base_path, file_name) for file_name in pdf_files]

    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)

    merger.write(base_path + "评审意见书-杜勇.pdf")
    merger.close()


if __name__ == "__main__":
    merge_pdf()
