from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionDirecionarVendas(Action):
    def name(self) -> Text:
        return "action_direcionar_vendas"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Simulando conexão com o sistema de vendas...")
        # Aqui você integraria com o subsistema de vendas.
        # Por exemplo, chamar uma API, abrir um novo canal, etc.
        # No nosso caso, é apenas uma mensagem de simulação.
        return []

class ActionDirecionarSuporte(Action):
    def name(self) -> Text:
        return "action_direcionar_suporte"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Simulando conexão com o sistema de suporte técnico...")
        # Aqui você integraria com o subsistema de suporte.
        return []

class ActionDirecionarInformacoes(Action):
    def name(self) -> Text:
        return "action_direcionar_informacoes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Simulando busca em base de conhecimento para informações gerais...")
        # Aqui você integraria com um sistema de informações ou KB.
        return []