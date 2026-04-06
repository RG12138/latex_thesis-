import PyPDF2
import sys

pdf_path = sys.argv[1]
output_path = sys.argv[2] if len(sys.argv) > 2 else None

reader = PyPDF2.PdfReader(pdf_path)
lines = [f'Pages: {len(reader.pages)}']
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        lines.append(f'--- Page {i+1} ---')
        lines.append(text)

result = '\n'.join(lines)
if output_path:
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result)
    print(f'Written to {output_path}')
else:
    print(result)
