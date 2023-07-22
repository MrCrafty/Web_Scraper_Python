import requests
from bs4 import BeautifulSoup as bs
URL = "https://realpython.github.io/fake-jobs/"

page = requests.get(URL)

soup = bs(page.content, 'html.parser')

results = soup.find(id="ResultsContainer")

job_elements = results.find_all('div', class_="card-content")

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower())

python_job_element = [
    h2_element.parent.parent.parent.find('p', class_="location") for h2_element in results.find_all(
        "h2", string=lambda text: "python" in text.lower())
]
