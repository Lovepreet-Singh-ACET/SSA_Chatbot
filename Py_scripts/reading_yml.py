from fileinput import filename
import yaml
import os
import pandas as pd

nlu_file_names = [
    "nlu-faq-agri-wheat-b0.yml"
]
domain_file_names = [
    "domain-agri-wheat-b0.yml"
]

questions_list = []
intent_names = []
for filename in nlu_file_names:
    if "agri" in filename or "hort" in filename:
        print(filename)

        with open("data/{}".format(filename)) as file:
            documents = yaml.full_load(file)
            # print(documents)
            for item, doc in documents.items():
                if item == "nlu":
                    # print(item, ":")
                    for i in range(len(doc)):
                        questions_list.append(doc[i]["examples"].split("\n")[0])
                        intent_names.append(doc[i]['intent'])
                        # print(doc[i]["examples"].split("\n")[0])
# print(intent_names)

print("Domain")
answer_list = []
second_answer_list = []
for filename in domain_file_names:
    if "agri" in filename or "hort" in filename:
        print(filename)
        
        with open("domain-grp/{}".format(filename)) as file:
            documents = yaml.full_load(file)
            # print(documents)
            for item, doc in documents.items():
                if item == "responses":
                    print(item, ":")
                    for intent in intent_names:
                        try:
                            # print(doc["utter_{}".format(intent)])
                            if len(doc["utter_{}".format(intent)]) == 1:
                                answer_list.append(doc["utter_{}".format(intent)][0]['text'])
                                second_answer_list.append(" ")
                            else:
                                answer_list.append(doc["utter_{}".format(intent)][0]['text'])
                                second_answer_list.append(doc["utter_{}".format(intent)][1]['text'])
                        except:
                            pass
                        # print(doc[i]["examples"].split("\n")[0])

df = pd.DataFrame({"questoions": questions_list, "answers": answer_list, "second_answer": second_answer_list})
df.to_csv("CSV/Added_Questions_Set_wheat_b0_new_data.csv", index=False)

print(len(questions_list), len(answer_list), len(second_answer_list))
# print(answer_list)