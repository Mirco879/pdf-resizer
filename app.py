from flask import Flask, request, send_file
import fitz  # PyMuPDF
from io import BytesIO

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "PDF Resizer API is running! Use POST /resize with a PDF file."

@app.route("/resize", methods=["POST"])
def resize_pdf():
    if "file" not in request.files:
        return "No file uploaded", 400

    uploaded_file = request.files["file"]
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    resized_doc = fitz.open()

    A4_WIDTH = 595  # A4 width in points
    for page in doc:
        scale_factor = A4_WIDTH / page.rect.width
        new_height = page.rect.height * scale_factor
        new_page = resized_doc.new_page(width=A4_WIDTH, height=new_height)
        new_page.show_pdf_page(new_page.rect, doc, page.number, keep_proportion=True)

    output_pdf = BytesIO()
    resized_doc.save(output_pdf)
    resized_doc.close()
    output_pdf.seek(0)

    return send_file(output_pdf, download_name="resized.pdf", as_attachment=True, mimetype="application/pdf")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)