# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
from typing import Any, Text, Dict, List
import urllib.request, json
import os
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# from fuzzywuzzy import fuzz
from textblob import TextBlob

# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []

class ActionGeneral(Action):

    def name(self) -> Text:
        return "action_general"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print("********************action_general**********************\n\n")
        _intent=tracker.latest_message['intent'].get('name')
        print(_intent)
        if _intent == "nlu_fallback":
            dispatcher.utter_message(response="utter_please_rephrase", buttons=[{"payload": "", "title": ""}])
        else:
            dispatcher.utter_message(response="utter_" + str(_intent), buttons=[{"payload": "", "title": ""}])
        return []

# class ActionSlotSetter(Action):
#     def name(self) -> Text:
#         return "action_slot_setter"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         buttons = [
#             {"payload":'/ok{"intent_button":"faq-agriculture"}',"title":"Agriculture"},
#             {"payload":'/ok{"intent_button":"faq-horticulture"}',"title":"Horticulture"}
#         ]
#         print(tracker.slots['intent_button'], "------------------------------")
#         if tracker.slots['intent_button'] == None:
#             print("\n","slots value is ",tracker.slots['intent_button'])
#             dispatcher.utter_message(text="Hi! Welcome to Farmerapp chatbot. For any queries related to crop, vegetation, etc, please select a topic from the below options.",buttons=buttons)
#         else:
#             print("\n","Now slots value is ",tracker.slots['intent_button'])
#             dispatcher.utter_message(text="Yes you are good to go")
#         return []

class ActionSlotSetter(Action):
    def name(self) -> Text:
        return "action_slot_setter"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons = [
            {"payload":'/ok{"intent_button":"faq-agriculture"}',"title":"Agriculture"},
            {"payload":'/ok{"intent_button":"faq-horticulture"}',"title":"Horticulture"}
        ]
        print(tracker.slots['intent_button'], "------------------------------")
        # if tracker.slots['intent_button'] == None:
        #     print("\n","slots value is ",tracker.slots['intent_button'])
        #     dispatcher.utter_message(text="Hi!! Welcome to SSA Punjab Bot. How can I help you??",buttons=buttons)
        # else:
        #     print("\n","Now slots value is ",tracker.slots['intent_button'])
        #     dispatcher.utter_message(text="Yes you are good to go")
        print("\n","slots value is ",tracker.slots['intent_button'])
        dispatcher.utter_message(text="Hi! Welcome to Farmerapp chatbot. For any queries related to crop, vegetation, etc, please select a topic from the below options.",buttons=buttons)
        return []

# class ActionVizFaq(Action):

#     def name(self) -> Text:
#         return "action_viz_faq"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         # print(tracker.latest_message)
#         buttons = [
#             {"payload":'/ok{"intent_button":"faq-agriculture"}',"title":"Agriculture"},
#             {"payload":'/ok{"intent_button":"faq-horticulture"}',"title":"Horticulture"}
#         ]
        
#         # dictionary for mapped retrieval intents
#         mapped_intent= { "faq-agriculture" : "Agriculture",
#                         "faq-horticulture":"Horticulture",
#                         None: "No-option"}

#         # to get a slot value (here --> slot is intent_button)
#         print("\n","Current Slots Value is: ",tracker.slots['intent_button']) 

#         if tracker.slots['intent_button'] ==None:
#             slot_value_clicked = mapped_intent[tracker.slots['intent_button']]
#         elif tracker.slots['intent_button'] == 'faq-agri-wheat':
#             slot_value_clicked = 'faq-agriculture'
#         elif tracker.slots['intent_button'] == 'faq-horti-wheat':
#             slot_value_clicked = 'faq-horticulture'
#         else:
#             slot_value_clicked = tracker.slots['intent_button']

#         # to get intent of user message
#         _intent=tracker.latest_message['intent'].get('name')
#         print("\nIntent of user message predicted by Rasa: ",_intent)

#         print("\nUser Message",tracker.latest_message['text']) # to get user typed message 

#         intent_found = json.dumps(tracker.latest_message['response_selector'][_intent]['ranking'][0]['intent_response_key'], indent=4)

#         second_intent_found = json.dumps(tracker.latest_message['response_selector'][_intent]['ranking'][1]['intent_response_key'], indent=4)
#         second_retrieval_intent_confidence = tracker.latest_message['response_selector'][_intent]['ranking'][1]['confidence']*100
#         # print('tracker latest message', tracker.latest_message['response_selector'])
#         # print(' ')
#         # print('---', tracker.latest_message['response_selector'].keys())
#         # print('   ')
#         print("\nretrieval we found (i.e intent response key ) ",intent_found)

#         # confidence of retrieval intent we found
#         retrieval_intent_confidence = tracker.latest_message['response_selector'][_intent]['response']['confidence']*100
#         print(f"\nRetrieval_intent_confidence we found was {retrieval_intent_confidence}")
#         # print("\nSecond Intent: ", second_intent_found, "\nConfidence: ", second_retrieval_intent_confidence)
#         if retrieval_intent_confidence < 80:
#             dispatcher.utter_message(text="I couldn't understand. Can you please rephrase it?")
#             return [SlotSet(key = "intent_button", value= [str(_intent[:-3])] ) ]

        
#         print("Intent: ", _intent,"Slot Clicked: ", slot_value_clicked[0])
#         if str(tracker.latest_message['text']) == str('https://forms.gle/Fk1TxTzAteigKFG87'):
#             dispatcher.utter_message(text='You can fill and submit the Google form')

#         elif _intent[4:8] == slot_value_clicked[0][4:8] :
#             """ if intent found is same as faq-visualisation or faq-portal or any other category
#             -3 tells we have left - and batch number 
#             ex from faq-visualisation-b0 we took faq-visualisation """


#         #used eval to remove quotes around the string
#             # print('intent before adding the utter', intent_found)
#             # print('----', eval(intent_found))
#             intent_found = f'utter_{eval(intent_found)}'
#             print('after adding utter we found -- ', intent_found)
#             dispatcher.utter_message(response = intent_found) # use response for defining intent name
#             # print("Difference: ",retrieval_intent_confidence - second_retrieval_intent_confidence)
#             if retrieval_intent_confidence - second_retrieval_intent_confidence <= 5:
#                 # print("in")
#                 dispatcher.utter_message(text="One more possible solution could be as below")
#                 dispatcher.utter_message(response=f'utter_{eval(second_intent_found)}')
#                 dispatcher.utter_message(text="Take decison as per your choice")
        
#         elif slot_value_clicked == 'No-option':
#             dispatcher.utter_message(text = "Please select any option first",buttons=buttons )
        
#         else:
#             # if retrieval_intent_confidence > 90:
#             intent_found = f'utter_{eval(intent_found)}'
            
#             dispatcher.utter_message(response = intent_found)
#             if _intent[4:8] == 'hort':
#                 domain = 'horticulture'
#             else:
#                 domain = 'agriculture' 
#             dispatcher.utter_message(text = f"Seems like you want to ask question from {domain} domain If yes you are good to go with that  but if you want to ask question from any other category please select a button",buttons=buttons)
            
#             tracker.slots['intent_button'] = _intent[:-3]
            
#             print(f"\nNow slot value is {tracker.slots['intent_button']}","\n")
#             print("---------------------------------------------------------")

#         return [SlotSet(key = "intent_button", value= [str(_intent[:-3])] ) ] # setting slot values

class ActionVizFaq(Action):

    def name(self) -> Text:
        return "action_viz_faq"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # print(tracker.latest_message)
        buttons = [
            {"payload":'/ok{"intent_button":"faq-agriculture"}',"title":"Agriculture"},
            {"payload":'/ok{"intent_button":"faq-horticulture"}',"title":"Horticulture"}
        ]
        
        # dictionary for mapped retrieval intents
        mapped_intent= { "faq-agriculture" : "Agriculture",
                        "faq-horticulture":"Horticulture",
                        None: "No-option"}

        # to get a slot value (here --> slot is intent_button)
        print("\n","Under viz faq slots value is ",tracker.slots['intent_button']) 
        
        if tracker.slots['intent_button'] ==None:
            slot_value_clicked = mapped_intent[tracker.slots['intent_button']]
        elif tracker.slots['intent_button'] == 'faq-agri-wheat':
            slot_value_clicked = 'faq-agriculture'
        elif tracker.slots['intent_button'] == 'faq-horti-wheat':
            slot_value_clicked = 'faq-horticulture'
        else:
            slot_value_clicked = tracker.slots['intent_button']

        # to get intent of user message
        _intent=tracker.latest_message['intent'].get('name')
        print("Intent of user message predicted by Rasa ",_intent)

        print(tracker.latest_message['text']) # to get user typed message 

        intent_found = json.dumps(tracker.latest_message['response_selector'][_intent]['ranking'][0]['intent_response_key'], indent=4)
        
        second_intent_found = json.dumps(tracker.latest_message['response_selector'][_intent]['ranking'][1]['intent_response_key'], indent=4)
        second_retrieval_intent_confidence = tracker.latest_message['response_selector'][_intent]['ranking'][1]['confidence']*100
        print("Second Intent: ", second_intent_found, "\nConfidence: ", second_retrieval_intent_confidence)
        # print('tracker latest message', tracker.latest_message['response_selector'])
        # print(' ')
        # print('---', tracker.latest_message['response_selector'].keys())
        # print('   ')
        print("retrieval we found (i.e intent response key ) ",intent_found)

        # confidence of retrieval intent we found
        retrieval_intent_confidence = tracker.latest_message['response_selector'][_intent]['response']['confidence']*100
        print(f"retrieval_intent_confidence we found was {retrieval_intent_confidence}")
        if retrieval_intent_confidence < 80:
            dispatcher.utter_message(text="I couldn't understand. Can you please rephrase it?", buttons=[{"payload": "", "title": ""}])
            return [SlotSet(key = "intent_button", value= [str(_intent[:-3])] ) ]

        
        print(_intent, slot_value_clicked[0])
        if str(tracker.latest_message['text']) == str('https://forms.gle/Fk1TxTzAteigKFG87'):
            dispatcher.utter_message(text='You can fill and submit the Google form', buttons=[{"payload": "", "title": ""}])

        elif _intent[4:8] == slot_value_clicked[0][4:8] :
            """ if intent found is same as faq-visualisation or faq-portal or any other category
            -3 tells we have left - and batch number 
            ex from faq-visualisation-b0 we took faq-visualisation """


        #used eval to remove quotes around the string
            # print('intent before adding the utter', intent_found)
            # print('----', eval(intent_found))
            intent_found = f'utter_{eval(intent_found)}'
            print('after adding utter we found -- ', intent_found)
            dispatcher.utter_message(response = intent_found, buttons=[{"payload": "", "title": ""}]) # use response for defining intent name
            print(retrieval_intent_confidence - second_retrieval_intent_confidence)
            if retrieval_intent_confidence - second_retrieval_intent_confidence <= 5:
                print("in")
                dispatcher.utter_message(text="One more possible solution could be as below", buttons=[{"payload": "", "title": ""}])
                dispatcher.utter_message(response=f'utter_{eval(second_intent_found)}', buttons=[{"payload": "", "title": ""}])
                dispatcher.utter_message(text="Take decison as per your choice", buttons=[{"payload": "", "title": ""}])
        
        elif slot_value_clicked == 'No-option':
            dispatcher.utter_message(text = "Please select any option first", buttons=buttons)
        
        else:
            # if retrieval_intent_confidence > 90:
            intent_found = f'utter_{eval(intent_found)}'
            
            dispatcher.utter_message(response = intent_found, buttons=[{"payload": "", "title": ""}])
            if _intent[4:8] == 'hort':
                domain = 'horticulture'
            else:
                domain = 'agriculture' 
            dispatcher.utter_message(text = f"Seems like you want to ask question from {domain} domain If yes you are good to go with that  but if you want to ask question from any other category please select a button",buttons=buttons)
            
            tracker.slots['intent_button'] = _intent[:-3]
            
            print(f"Now slot value is {tracker.slots['intent_button']}","\n")

        return [SlotSet(key = "intent_button", value= [str(_intent[:-3])] ) ] # setting slot values

class ActionLanguageDetectorRetrieval(Action):

    def name(self) -> Text:
        return "action_language_detector_retrieval"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print('Language detector for Retrieval')
        # to get intent of user message
        _intent=tracker.latest_message['intent'].get('name')
        print("Intent of user message predicted by Rasa ",_intent)

        text = tracker.latest_message['text'] # to get user typed message
        lang = TextBlob(text)
        lang = lang.detect_language()
        print("Language of user message is ",lang)
        if lang == _intent[-2:]:
            # print(lang,_intent[-2:])
            # dispatcher.utter_message(f"Your message is in {lang}")
            ls_of_lang_intent = []
            intent_found = json.dumps(tracker.latest_message['response_selector'][_intent]['ranking'], indent=4)
            print(intent_found)
            intent_found = json.loads(intent_found)
            for lang_finder_iter in intent_found:
                print(lang_finder_iter['intent_response_key'])
                if lang_finder_iter['intent_response_key'].split('/',1)[0][-2:] == lang:
                    ls_of_lang_intent.append(lang_finder_iter)
            print("\n","ls_of_lang_intent",ls_of_lang_intent)
            
        #     # sorting needed to get the highest confidence intent
        print("retrieval we found (i.e intent response key ) ",ls_of_lang_intent[0]['intent_response_key'])
        intent_found = ls_of_lang_intent[0]['intent_response_key']

        intent_found = 'utter_'+str(intent_found)
        print('after adding utter we found -- ', intent_found)
        dispatcher.utter_message(response=intent_found)
        return [SlotSet('language', lang)]