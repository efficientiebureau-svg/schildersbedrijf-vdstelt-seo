from pathlib import Path
places = [('Raamsdonksveer', 'schilder-raamsdonksveer'), ('Geertruidenberg', 'schilder-geertruidenberg'), ('Raamsdonk', 'schilder-raamsdonk'), ('Oosterhout', 'schilder-oosterhout'), ('Made', 'schilder-made'), ('Drimmelen', 'schilder-drimmelen'), ('Wagenberg', 'schilder-wagenberg'), ('Terheijden', 'schilder-terheijden'), ('Dongen', 'schilder-dongen'), ('Waspik', 'schilder-waspik'), ('Breda', 'schilder-breda'), ('Waalwijk', 'schilder-waalwijk'), ('Kaatsheuvel', 'schilder-kaatsheuvel'), ('Loon op Zand', 'schilder-loon-op-zand'), ('Sprang-Capelle', 'schilder-sprang-capelle'), ('Rijen', 'schilder-rijen'), ('Gilze', 'schilder-gilze'), ('Tilburg', 'schilder-tilburg'), ('Etten-Leur', 'schilder-etten-leur'), ('Zevenbergen', 'schilder-zevenbergen'), ('Teteringen', 'schilder-teteringen'), ('Prinsenbeek', 'schilder-prinsenbeek'), ('Lage Zwaluwe', 'schilder-lage-zwaluwe'), ('Hooge Zwaluwe', 'schilder-hooge-zwaluwe'), ('Moerdijk', 'schilder-moerdijk'), ('Klundert', 'schilder-klundert'), ('Hank', 'schilder-hank'), ('Dussen', 'schilder-dussen'), ('Werkendam', 'schilder-werkendam'), ('Sleeuwijk', 'schilder-sleeuwijk'), ('Almkerk', 'schilder-almkerk'), ('Nieuwendijk', 'schilder-nieuwendijk')]
template = Path("content/seo/templates/local-landing-template.md").read_text()
out_dir = Path("content/seo/pages/plaatsen"); out_dir.mkdir(parents=True, exist_ok=True)
for place, slug in places:
    content = template.replace("{plaats}", place).replace("{slug}", slug)
    (out_dir / f"{slug}.md").write_text(content)
    print(out_dir / f"{slug}.md")
