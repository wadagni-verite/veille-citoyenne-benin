#!/usr/bin/env python3
import json
import sys

def validate():
    with open('data/content.json', 'r') as f:
        data = json.load(f)
    
    errors = []
    
    # Vérifier que chaque personne est liée à une affaire existante
    for personne in data['personnalites']:
        affaire_ids = [a['id'] for a in data['affaires']]
        if personne.get('affaireId') not in affaire_ids:
            errors.append(f"❌ {personne['nom']} lié à une affaire inexistante")
    
    # Vérifier que les liens Dropbox sont valides
    for affaire in data['affaires']:
        for preuve in affaire.get('preuves', []):
            if 'dropbox.com' not in preuve['lien']:
                errors.append(f"⚠️ Lien non-Dropbox: {preuve['titre']}")
    
    # Vérifier les dates (format cohérent)
    # ... autres règles métier ...
    
    if errors:
        print("ERREURS DE COHÉRENCE:")
        for e in errors:
            print(e)
        sys.exit(1)
    else:
        print("✅ Données cohérentes")
        sys.exit(0)

if __name__ == "__main__":
    validate()
