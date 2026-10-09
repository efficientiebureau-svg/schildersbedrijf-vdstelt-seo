# Schildersbedrijf vd Stelt — SEO content pack

Lokale SEO-uitbreiding voor `schildersbedrijfvdstelt.nl`:

- hoofdpagina-copy
- dienstenpagina's
- lokale AIDA-landingspagina's rondom Raamsdonksveer
- blogplanning en blogdrafts
- JSON-LD structured data/rich snippets
- metadata-map en interne linking-map
- statische preview via GitHub Pages

## Preview
Open `index.html` lokaal of via GitHub Pages zodra Pages actief is.

## Validatie
```bash
python3 scripts/validate-seo-content.py
python3 -m json.tool content/seo/structured-data/local-business.json >/dev/null
python3 -m json.tool content/seo/structured-data/faq-home.json >/dev/null
```
