#! python3
import docx

def get_text(file_name):
    document = docx.Document(file_name)
    full_text = list()
    for paragraph in document.paragraphs:
        full_text.append('  ' + paragraph.text)

    return '\n\n'.join(full_text)
