import random
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, UserUtteranceReverted

class ActionScheduleMeeting(Action):
    def name(self) -> Text:
        return "action_schedule_meeting"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Example code to schedule a meeting
        dispatcher.utter_message(text="Meeting has been scheduled.")
        return [SlotSet("meeting_scheduled", True)]

class ActionSendCustomMessage(Action):
    def name(self) -> Text:
        return "action_send_custom_message"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Logic to handle sending a custom message
        dispatcher.utter_message(text="Your custom message has been sent.")
        return []
class ActionUtterRandomGoodbye(Action):

    def name(self) -> Text:
        return "action_utter_random_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        goodbye_messages = [
            "See you later!",
            "Take care!",
            "Farewell!",
            "Catch you later!",
            "Have a good one!",
            "Adios!",
            "Until next time!",
            "Peace out!",
            "Goodbye for now!",
            "Talk to you soon!",
            "So long!",
            "See you soon!",
            "Later, alligator!",
            "Bye for now!",
            "Take it easy!",
            "Cheerio!",
            "Ciao!",
            "Till we meet again!",
            "Be well!",
            "Bye-bye!"
        ]

        message = random.choice(goodbye_messages)
        dispatcher.utter_message(text=message)

        return []
class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Handling fallback actions
        last_intent = tracker.latest_message['intent'].get('name')
        if last_intent in ["request_schedule_meeting", "send_message"]:
            dispatcher.utter_message(text="I'm sorry, I didn't understand that. Please specify if you want to schedule a meeting or send a message.")
        else:
            dispatcher.utter_message(text="I'm sorry, I didn't understand that. Could you please rephrase?")
        return [UserUtteranceReverted()]
