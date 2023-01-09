# Import necessary modules
from aspose.pdf import Document
from aspose.pdf.saving import XmlSaveOptions

def convert_PDF_to_XML(infile, outfile):
    # Open PDF document
    document = Document(infile)

    # Instantiate XML Save options
    save_options = XmlSaveOptions()

    # Save the XML document
    document.save(outfile, save_options)

# Convert the PDF file
convert_PDF_to_XML('input.pdf', 'output.xml')
