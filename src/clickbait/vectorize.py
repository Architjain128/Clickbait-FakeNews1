import json
import spacy

nlp = spacy.load("en_core_web_lg")

# for lg the dimensions are 300, checked by adding print statement

if __name__ == '__main__':
    f = open('../../dataset/clickbait_dataset/processed_string20k.json','r')
    data = json.load(f)
    newData = {}
    c = 0
    for i in data:
        vectors = nlp(data[i][0])
        newList = []
        for j in vectors.vector:
            newList.append(float(j))
        newData[i] = []
        newData[i].append(data[i][1])
        newData[i].append(newList)
        
        c += 1
        print(c)

        # print(type(data), type(data[i]))
        # break
    with open('../../dataset/clickbait_dataset/300dims_vectorized_spacy20k.json', 'w') as f:
        json.dump(newData, f)