import os
import re

TEMPLATES_DIR = 'app/templates'
OUTPUT_DIR = 'site_dist'

# Fichiers à ignorer (inclusions)
IGNORED = {'base.html', 'Header.html', 'Footer.html'}

# Chargement des fragments
with open(os.path.join(TEMPLATES_DIR, 'base.html'), encoding='utf-8') as f:
    base_html = f.read()
with open(os.path.join(TEMPLATES_DIR, 'Header.html'), encoding='utf-8') as f:
    header_html = f.read()
with open(os.path.join(TEMPLATES_DIR, 'Footer.html'), encoding='utf-8') as f:
    footer_html = f.read()

def extract_block(content, block_name):
    # Extrait le contenu d'un bloc Jinja
    pattern = re.compile(r'{% block ' + re.escape(block_name) + r' %}(.*?){% endblock %}', re.DOTALL)
    match = pattern.search(content)
    return match.group(1).strip() if match else ''

def replace_url_for(text):
    # Remplace {{ url_for('nom') }} par nom.html
    return re.sub(r"{{\s*url_for\('([a-zA-Z0-9_]+)'\)\s*}}", r"\1.html", text)

def render_static_page(template_name):
    with open(os.path.join(TEMPLATES_DIR, template_name), encoding='utf-8') as f:
        content = f.read()
    # Titre
    title = extract_block(content, 'title') or 'TrashUP'
    # Explication
    explanation = extract_block(content, 'explanation')
    # Contenu principal
    main_content = extract_block(content, 'content')
    # Si pas de blocs, tout le contenu (AboutUs, etc)
    if not explanation and not main_content:
        main_content = content
    # Remplacement des liens dynamiques
    explanation = replace_url_for(explanation)
    main_content = replace_url_for(main_content)
    # Header/Footer statiques
    header = replace_url_for(header_html)
    footer = footer_html
    # Construction de la page
    page = base_html
    page = page.replace('{% include \'Header.html\' %}', header)
    page = page.replace('{% include \'Footer.html\' %}', footer)
    page = re.sub(r'{% block title %}.*?{% endblock %}', title, page, flags=re.DOTALL)
    page = re.sub(r'{% block explanation %}.*?{% endblock %}', explanation, page, flags=re.DOTALL)
    page = re.sub(r'{% block content %}.*?{% endblock %}', main_content, page, flags=re.DOTALL)
    # Suppression des balises Jinja restantes
    page = re.sub(r'{%.*?%}', '', page)
    page = re.sub(r'{{.*?}}', '', page)
    return page

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for filename in os.listdir(TEMPLATES_DIR):
        if filename.endswith('.html') and filename not in IGNORED:
            static_html = render_static_page(filename)
            with open(os.path.join(OUTPUT_DIR, filename), 'w', encoding='utf-8') as f:
                f.write(static_html)
    print(f"Conversion terminée. Fichiers statiques dans {OUTPUT_DIR}/")

if __name__ == '__main__':
    main() 