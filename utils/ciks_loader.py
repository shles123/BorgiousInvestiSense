def load_ciks(file_path):
    ciks = []
    with open(file_path, 'r') as file:
            for line in file:
                cik, name = line.split(':')   
                ciks.append(cik.strip())
    return ciks


if __name__ == "__main__":
    ciks = load_ciks('../data/CIK.txt')
    print(ciks)