from langchain_community.document_loaders import PyPDFLoader

def extract_text_from_pdf(pdf_path):
    """
    Extrae el texto de un archivo PDF utilizando PyPDFLoader.
    :param pdf_path: Ruta del archivo PDF
    :return: Texto extraído del PDF
    """
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    return "\n".join([page.page_content for page in pages])
