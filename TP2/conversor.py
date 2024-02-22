import sys
import re

md = sys.stdin.read()

# Titulos
md = re.sub(r'^#\s+(.*)$', r'<h1>\1</h1>', md, flags=re.MULTILINE)
md = re.sub(r'^##\s+(.*)$', r'<h2>\1</h2>', md, flags=re.MULTILINE)
md = re.sub(r'^###\s+(.*)$', r'<h3>\1</h3>', md, flags=re.MULTILINE)

# Listas
md = re.sub(r'^\+\s+(.*)$', r'<li>\1</li>', md, flags=re.MULTILINE)
md = re.sub(r'^\*\s+(.*)$', r'<li>\1</li>', md, flags=re.MULTILINE)

# Separador Horizontal
md = re.sub(r'^---$', r'<hr>', md, flags=re.MULTILINE)

# Links
md = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', md)

# Imagens
md = re.sub(r'!\[([^\]]+)\]\(([^)]+)\)', r'<img src="\2" alt="\1">', md)

# Codigo
md = re.sub(r'```\s*([^`]+)\s*```', r'<pre><code>\1</code></pre>', md, flags=re.MULTILINE)

# Blockquote
md = re.sub(r'^>\s+(.*)$', r'<blockquote>\1</blockquote>', md, flags=re.MULTILINE)

# Italico
md = re.sub(r'\b_(.*?)_\b', r'<em>\1</em>', md)

# Negrito
md = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', md)

# Riscado
md = re.sub(r'~~(.*?)~~', r'<del>\1</del>', md)

# Lista de Tarefas
md = re.sub(r'- \[ \] (.*)', r'<input type="checkbox" disabled> \1', md)
md = re.sub(r'- \[x\] (.*)', r'<input type="checkbox" disabled checked> \1', md)

# Tabela

# Bloco de Codigo
md = re.sub(r'```\s*([^`]+)\s*```', r'<pre><code>\1</code></pre>', md, flags=re.MULTILINE)

# Output the HTML
sys.stdout.write("<!DOCTYPE html><html><head><title>Page Title</title></head><body>")
sys.stdout.write(md)
sys.stdout.write("</body></html>\n")
