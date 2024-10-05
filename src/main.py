from edgar_api import fetch_filing_forms
from utils import load_ciks

def main():
    ciks = load_ciks('../data/CIK.txt')
    print(ciks[0])
    form  = fetch_filing_forms(ciks[0])
    if form:
        print(form)
    # for cik in ciks:
    #     forms = fetch_filing_forms(cik)
    #     if forms:
    #         print(f"Fetched 13F forms for CIK {cik}:")
    #         print(forms)

if __name__ == "__main__":
    main()