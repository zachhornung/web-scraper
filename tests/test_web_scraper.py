from web_scraper.scraper import Scraper


def test_import():
    assert Scraper
    
def test_scraping_abilities_count():
    url = 'https://en.wikipedia.org/wiki/Roman_Empire'
    scraper = Scraper()
    assert scraper.get_citations_needed_count(url) == 2
    
def test_scraping_abilities_paragraph():
    url = 'https://en.wikipedia.org/wiki/Roman_Empire'
    scraper = Scraper()
    assert scraper.get_citations_needed_report(url) == 'Temples housed the cult images of deities, often by famed sculptors.[482] The religiosity of the Romans encouraged the production of decorated altars, small representations of deities for the household shrine or votive offerings, and other pieces for dedicating at temples. Divine and mythological figures were also given secular, humorous, and even obscene depictions.[citation needed]\n------------\nMuch of what is known of Roman painting is based on the interior decoration of private homes, particularly as preserved at Pompeii and Herculaneum by the eruption of Vesuvius in 79 AD. In addition to decorative borders and panels with geometric or vegetative motifs, wall painting depicts scenes from mythology and the theatre, landscapes and gardens, recreation and spectacles, work and everyday life, and frank pornography. Birds, animals, and marine life are often depicted with careful attention to realistic detail.[citation needed]'
