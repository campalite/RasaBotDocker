# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.events import Restarted
from rasa_sdk.executor import CollectingDispatcher

class ActionStartSession(Action):
    def name(self) -> Text:
        return "action_start_session"

    def run(
        self,
        dispatcher:"CollectingDispatcher",
        tracker: Tracker,
        domain:"DomainDict",
    ) -> List[Dict[Text,Any]]:
        return [SlotSet("is_logged_in",True)]

class ActionCarousel(Action):
    def name(self) -> Text:
        return "action_carousels"
    
    def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Merhaba, bugün nasılsın?",
                        "subtitle": "$10",
                        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqhmyBRCngkU_OKSL6gBQxCSH-cufgmZwb2w&usqp=CAU",
                        "buttons": [ 
                            {
                            "title": "Muhteşem",
                            "payload": "muhteşem",
                            "type": "postback"
                            },
                            {
                            "title": "kötü",
                            "payload": "Kötü",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Carousel 2",
                        "subtitle": "$12",
                        "image_url": "https://image.freepik.com/free-vector/city-illustration_23-2147514701.jpg",
                        "buttons": [ 
                            {
                            "title": "Click here",
                            "url": "https://image.freepik.com/free-vector/city-illustration_23-2147514701.jpg",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []


class ActionRestart(Action):

    def name(self) -> Text:
        return "action_restart"

    async def run(
        self,dispatcher,tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

    # custom_behavior

        return [Restarted()]