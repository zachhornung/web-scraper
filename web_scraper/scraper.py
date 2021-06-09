import requests, re
from bs4 import BeautifulSoup


class Scraper:
  def __init__(self):
    self.num_citations = None
    self.citation_passages = None
    
  def scrape(self, url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    paragraphs = soup.find_all("p")
    citations_needed = [p for p in paragraphs if 'citation needed' in p.text]
    citations_needed = [re.sub('<.*?>', '', str(p)) for p in citations_needed]
    citations_needed = [re.sub('\\n', '', p) for p in citations_needed]
    self.citation_passages = citations_needed 
    self.num_citations = len(citations_needed)
  
  def get_citations_needed_count(self, url=None):
    if (self.num_citations == None) or url:
      self.scrape(url)
    return self.num_citations

  def get_citations_needed_report(self, url=None):
    if (self.citation_passages == None) or url:
      self.scrape(url)
    return '\n------------\n'.join(self.citation_passages)
  
  
if __name__=='__main__':
  scraper = Scraper()
  goats = scraper.get_citations_needed_report('https://en.wikipedia.org/wiki/House_of_Romanov')
  print(goats)