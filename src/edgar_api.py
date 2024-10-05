import requests

def fetch_filing_forms(cik):
    url = f'https://data.sec.gov/submissions/CIK{cik}.json'

    response = requests.get(url, headers={'User-Agent': 'Noah Schles (noah.njs@gmail.com)'})

    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch data for CIK: {cik}. Status code: {response.status_code}")
        return None
    