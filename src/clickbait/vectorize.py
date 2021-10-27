import json
import spacy

nlp = spacy.load("en_core_web_sm")

if __name__ == '__main__':
    f = open('../../dataset/clickbait_dataset/processed_string10k.json','r')
    data = json.load(f)
    newData = {}
    for i in data:
        vectors = nlp(data[i][0])
        newList = []
        for j in vectors.vector:
            newList.append(float(j))
        newData[i] = []
        newData[i].append(data[i][1])
        newData[i].append(newList)

        # print(type(data), type(data[i]))
        # break
    with open('../../dataset/vectorized_temp.json', 'w') as f:
        json.dump(newData, f)
        # break
