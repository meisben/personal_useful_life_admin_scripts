
# --------------------------------------------------------------------
# Author: Ben Money-Coomes
# Purpose: A collated collection of functions to edit pdfs from python
#
# --- Credit ---
# Source for information: PyPDF4 documentation
# Source for information 2: https://realpython.com/pdf-python/
#
# --------------------------------------------------------------------


import os
from PyPDF4 import PdfFileReader, PdfFileWriter

CODE_SNIPPETS_ROOT = os.path.dirname(__file__)
INPUT_PDF_ROOT = os.path.join(CODE_SNIPPETS_ROOT, "pdfInputs")
OUTPUT_PDF_ROOT = os.path.join(CODE_SNIPPETS_ROOT, "pdfOutputs")


def extract_pdf_information(pdf_path):
    """ Print and return pdf information
    """
    # read binary
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    txt = f"""
    Information about {pdf_path}: 

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """

    print(txt)
    return information


def rotate_pages_and_write_example(pdf_path):
    """ Rotate pages and write
    """
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(pdf_path)
    # Rotate page 90 degrees to the right
    page_1 = pdf_reader.getPage(0).rotateClockwise(90)
    pdf_writer.addPage(page_1)
    # Rotate page 90 degrees to the left
    page_2 = pdf_reader.getPage(1).rotateCounterClockwise(90)
    pdf_writer.addPage(page_2)
    # Add a page in normal orientation
    pdf_writer.addPage(pdf_reader.getPage(2))

    with open('rotate_pages.pdf', 'wb') as fh:
        pdf_writer.write(fh)


def merge_pdfs(paths, output):
    """ Merges and writes pages
    """
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)


def split_to_single_pages(path, name_of_split):
    """ Splits one document into single pages
    """
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output = f'{name_of_split}{page}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

# -----------------BMC Defined functions ----------------


def write_pdf_subset(input_path, output_path, page_start, page_end):
    pdf_writer = PdfFileWriter()

    pdf_reader = PdfFileReader(input_path)

    if pdf_reader.getNumPages() < page_end:
        Exception("too few pages")

    for page in range(page_start, page_end):
        # Add each page to the writer object
        pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output_path, 'wb') as out:
        pdf_writer.write(out)


def add_pdf_subset(pdf_writer, input_path, page_start, page_end):
    my_pdf_writer = pdf_writer

    pdf_reader = PdfFileReader(input_path)

    if pdf_reader.getNumPages() < page_end:
        Exception("too few pages")

    for page in range(page_start, page_end):
        # Add each page to the writer object
        my_pdf_writer.addPage(pdf_reader.getPage(page))


def write_pdf_object(my_pdf_writer, pdf_output_path):
    """ Rotate a single pdf page 
    """
    with open(pdf_output_path, 'wb') as fh:
        my_pdf_writer.write(fh)


# -----------------End of BMC Defined functions ----------------

if __name__ == '__main__':

    input_name = "Dissertation_MSc_Robotics_v30thJuly.pdf"
    input_path = os.path.join(INPUT_PDF_ROOT, input_name)

    output_name = "dissertation_introduction_section.pdf"
    output_path = os.path.join(OUTPUT_PDF_ROOT, output_name)

    extract_pdf_information(input_path)

    # write_pdf_subset(input_path, output_path, 0, 3)

    pdf_writer = PdfFileWriter()

    add_pdf_subset(pdf_writer, input_path, 0, 1)  # contents page
    add_pdf_subset(pdf_writer, input_path, 14, 23)  # introduction section
    add_pdf_subset(pdf_writer, input_path, 50, 56)  # bibliography section

    write_pdf_object(pdf_writer, output_path)
