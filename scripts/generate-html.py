#!/usr/bin/env python3
import json
import os
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

def generate_site():
    # 1. Charger les données
    with open('data/content.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 2. Configurer Jinja2
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('index-template.html')
    
    # 3. Rendu avec les données
    html_output = template.render(
        affaires=data['affaires'],
        personnalites=data['personnalites'],
        institutions=data['institutions'],
        stats=data['statistiques'],
        association=data['association'],
        navigation=data.get('navigation', [
            {"id": "accueil", "label": "Accueil", "icon": "shield"},
            {"id": "institutions", "label": "Institutions", "icon": "building-2"},
            {"id": "personnalites", "label": "Personnalités", "icon": "users"},
            {"id": "documents", "label": "Documents", "icon": "file-text"},
            {"id": "cas", "label": "Cas Documentés", "icon": "alert-triangle"},
            {"id": "mentions-legales", "label": "Mentions Légales", "icon": "file-text"},
            {"id": "partager", "label": "Partager", "icon": "share-2"}
        ]),
        current_year=datetime.now().year,
        last_updated=data['metadata']['lastUpdated']
    )
    
    # 4. Sauvegarder dans docs/ pour GitHub Pages
    os.makedirs('docs', exist_ok=True)
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(html_output)
    
    print(f"✅ Site généré: docs/index.html ({len(html_output):,} caractères)")
    print(f"📊 {len(data['affaires'])} affaire(s), {len(data['personnalites'])} personne(s), {len(data['institutions'])} institution(s)")

if __name__ == "__main__":
    generate_site()
