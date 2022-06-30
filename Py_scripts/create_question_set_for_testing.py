from fileinput import filename
import yaml
import os
import pandas as pd

nlu_file_names = [ "/home/ubuntu/SSA/SSA_Chatbot/data/nlu-faq-agri-wheat-b4.yml" ]
domain_file_names = ["/home/ubuntu/SSA/SSA_Chatbot/domain-grp/domain-agri-wheat-b4.yml"]

questions_list = []
intent_names = []
sentences = []
for filename in nlu_file_names:
    with open(filename) as file:
        documents = yaml.full_load(file)
        # print(documents)
        for item, doc in documents.items():
            if item == "nlu":
                # print(item, ":")
                for i in range(len(doc)):
                    for sen in doc[i]["examples"].split("\n"):
                        # print(sen[2:])
                        # print()
                        # print(doc[i]['intent'])
                        if len(sen) > 1:    
                            intent_names.append(doc[i]['intent'])
                            sentences.append(sen[2:])
                        # questions_list.append()
                        # intent_names.append(doc[i]['intent'])
print(len(intent_names))
print(len(sentences))
print("Domain")

answer_list = []
second_answer_list = []
for filename in domain_file_names:        
    with open(filename) as file:
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

print(len(answer_list))
df = pd.DataFrame(
    { "questoions": sentences,
      "answers": answer_list
      })
df.to_csv("/home/ubuntu/SSA/SSA_Chatbot/CSV/wheat_b4_data_for_translation.csv", index=False)

# print(len(questions_list), len(answer_list), len(second_answer_list))
# print(answer_list)