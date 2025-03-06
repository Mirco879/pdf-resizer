import fitz  # PyMuPDF

# Define A4 dimensions in points (1 point = 1/72 inch)
A4_WIDTH = 595  # width in points for A4 size (210 mm)

# Input and output paths
input_pdf_path = "air-2025-lecture1ab.pdf"
# output_pdf_path = '03c-classification_III_resized.pdf'

output_pdf_path = input_pdf_path
#
# Open the original PDF and create a new, empty PDF for resized pages
doc = fitz.open(input_pdf_path)
resized_doc = fitz.open()

# Resize each page
for page_num in range(len(doc)):
    page = doc[page_num]
    # Get the current page dimensions
    width, height = page.rect.width, page.rect.height
    
    # Calculate scaling factor to fit the width to A4
    scale_factor = A4_WIDTH / width
    new_height = height * scale_factor  # Scale height proportionally
    
    # Create a new page in the resized document with A4 width and scaled height
    new_page = resized_doc.new_page(width=A4_WIDTH, height=new_height)
    
    # Insert the original page content into the new page with scaling
    new_page.show_pdf_page(new_page.rect, doc, page_num, keep_proportion=True)

# Save the resized PDF
resized_doc.save(output_pdf_path)
resized_doc.close()
doc.close()

print("Resized PDF saved as:", output_pdf_path)