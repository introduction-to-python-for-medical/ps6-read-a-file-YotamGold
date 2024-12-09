def create_codon_dict(file_path):
    file = open(file_path, "r")
    rows = file.readlines()
    file.close()
    myD = {}
    for row in rows:
      cell = row.strip().split('\t')
      myD[cell[0]] = cell [2] 
    return myD
