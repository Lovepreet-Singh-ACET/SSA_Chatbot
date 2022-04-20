import pandas as pd
import pprint

pp = pprint.PrettyPrinter(indent=4)
data = pd.read_csv("pun_data/wheat_b5_punjabi.csv")

# print(data.columns)
# ['question', 'answer', 'Punjabi Question', 'Punjabi Answer']

# print(data.head())
print(data['answer'].nunique())

df_sliced_dict = {}

for ans in data['answer'].unique():
    df_sliced_dict[ans] = data[data['answer'] == ans]

intent_name = "faq-agri-wheat-b5-pun"

with open("data/nlu-faq-agri-wheat-b5-pun.yml", "w") as file, open("domain-grp/domain-agri-wheat-b5-pun.yml", "w") as file2:
    file.write("version: \"3.0\"\n")
    file.write("nlu:\n")

    file2.write("version: \"3.0\"\n\n")
    file2.write("intents:\n")
    file2.write(f"  - {intent_name}\n\n")
    file2.write("responses:\n")
    for key in df_sliced_dict.keys():
        print(key)
        # break
        name = df_sliced_dict[key]['question'].iloc[0].strip().replace(" ", "-")                          #key.strip()[::5].replace(" ", "-")
        file.write(f"- intent: {intent_name}/{name}\n")
        file.write("  examples: |\n")

        file2.write(f"  utter_{intent_name}/{name}:\n")

        # print(df_sliced_dict[key].columns)
        # break
        # for df_key in df_sliced_dict[key]:
        df_key = df_sliced_dict[key].copy()
        # print(df_key)
        # break
        lst = df_key['Punjabi Question'].tolist()
        string = "    - "+"\n    - ".join(lst) + "\n"
        file.write(string)

        answer = df_key["Punjabi Answer"].iloc[0]
        file2.write(f"  - text: {answer}\n")
