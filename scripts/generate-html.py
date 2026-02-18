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
        navigation=data.get('navigation', []), # Ajout de la navigation si présente
        current_year=datetime.now().year,
        last_updated=data['metadata']['lastUpdated']
    )
    
    # 4. Sauvegarder le fichier final dans le dossier /docs
    # C'est ici que le changement est crucial pour GitHub Pages
    os.makedirs('docs', exist_ok=True)
    output_file = 'docs/index.html'
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_output)
    
    print(f"✅ Site généré avec succès dans : {output_file}")
    print(f"📊 Statistiques : {data['statistiques']['affaires']} affaire(s), {data['statistiques']['personnes']} personne(s)")

if __name__ == "__main__":
    generate_site()
