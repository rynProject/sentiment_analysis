import pandas as pd
import nltk
import re
import string
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

df = pd.read_excel("DATAOLAHbaru.xlsx",sheet_name=0)

lst = []
for i in df.index:
    data = df['text'][i]
    kalimat1 = data
    case_folding = kalimat1.lower()
    case_folding2 = re.sub(r"\d+", "", case_folding)
    kalimat = case_folding2.translate(str.maketrans("", "", string.punctuation))
    caseFolding = []
    caseFolding.append('case folding')
    caseFolding.append(kalimat)
    print(kalimat)

    tokenization = []
    tokens = nltk.tokenize.word_tokenize(kalimat)
    kemunculan = nltk.FreqDist(tokens)
    tokenization.append('Tokenization')

    for kmost in kemunculan.most_common():
        tokenization.append(kmost)

    print(tokenization)

    lst.append(caseFolding)
    lst.append(tokenization)
    kalimat = kalimat.translate(str.maketrans('', '', string.punctuation)).lower()
    tokens = word_tokenize(kalimat)
    listStopword = set(stopwords.words('indonesian'))
    removed = []
    filtering = []
    filtering.append('Filtering')
    for t in tokens:
        if t not in listStopword:
            removed.append(t)
            filtering.append(t)
            print(filtering)
    lst.append(filtering)
    df1 = pd.DataFrame(lst)
    df1.to_excel("outputterbaru1.xlsx")  #