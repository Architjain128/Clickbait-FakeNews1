import json
import spacy

nlp = spacy.load("en_core_web_sm")

if __name__ == '__main__':
    f = open('dataset/processed_string10k.json','r')
    data = json.load(f)

    for i in data:
        vectors = nlp(data[i][0])
        newList = []
        for j in vectors.vector:
            newList.append(float(j))
        data[i].append(newList)

        # print(type(data), type(data[i]))
        # break
    with open('dataset/vectorized_spacy10k.json', 'w') as f:
        json.dump(data, f)
        # break
