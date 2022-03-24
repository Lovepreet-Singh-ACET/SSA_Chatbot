"""
This file is used to test the questions
"""
import requests
import json
import pandas as pd

data = pd.read_csv("/home/ubuntu/SSA/SSA_Chatbot/CSV/test_set_rice_b2.csv")
# print(data)
question_list = []
original_answer_list = []
bot_answer_list = []
confidence_list = []
correct_pred_or_not = []
for index, row in data.iterrows():
    question = row["questoions"]
    orig_ans = row["answers"]

    payload = json.dumps(dict(sender="rasa", message=question))
    payload2 = json.dumps(dict(message_id="rasa", text=question))
    # print(payload)
    try:
        r = requests.post( url='http://localhost:5005/webhooks/rest/webhook', data=payload)
        r2 = requests.post( url='http://localhost:5005/model/parse', data=payload2)
        # print(r)
        # response = json.loads(r)
        # print(r.text)
        # print(r.json()[0]["text"])
        # response = json.loads(r2)
        # print(r2.json()['response_selector']['nlu-faq-weho-parking-b1']['response']['responses'][0]['text'])
        _intent=r2.json()['intent']['name']
        print(_intent)
        confidence = r2.json()['response_selector'][_intent]['response']['confidence']
        answer = r.json()[0]["text"]
        question_list.append(question)
        original_answer_list.append(orig_ans)
        bot_answer_list.append(answer)
        confidence_list.append(confidence)
        correct_pred_or_not.append(answer == orig_ans)

        print('predicted answer - ', answer)
        print('original answer - ', orig_ans)
        print('confidence -', confidence)
    except:
        pass

df = pd.DataFrame({"question": question_list, "bot_answer": bot_answer_list, "orginal_answer": original_answer_list , "confidence": confidence_list, "Correct": correct_pred_or_not})
df.to_csv("/home/ubuntu/SSA/SSA_Chatbot/test_results/test_set_rice_b2_results.csv", index=False)