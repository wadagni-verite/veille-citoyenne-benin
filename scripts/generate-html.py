#!/usr/bin/env python3
import json
import os
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

def generate_site():
    # Charger les données
    with open('data/content.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Configurer Jinja2
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('index-template.html')
    
    # Rendu avec les données
    html_output = template.render(
        affaires=data['affaires'],
        personnalites=data['personnalites'],
        institutions=data['institutions'],
        stats=data['statistiques'],
        association=data['association'],
        current_year=datetime.now().year,
        last_updated=data['metadata']['lastUpdated']
    )
    
    # Sauvegarder le fichier final
    os.makedirs('output', exist_ok=True)
    with open('output/index.html', 'w', encoding='utf-8') as f:
        f.write(html_output)
    
    print(f"✅ Site généré: output/index.html ({len(html_output)} caractères)")
    print(f"📊 {len(data['affaires'])} affaire(s), {len(data['personnalites'])} personne(s)")

if __name__ == "__main__":
    generate_site()
