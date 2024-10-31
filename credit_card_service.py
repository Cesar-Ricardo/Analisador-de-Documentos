from azure.core.credentils import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRquest
from ultils.Config import Config

def analize_credit_card(card_url):
        
    credential = AzureKeyCredential(Config.KEY)

    document_Client = DocumentIntelligenceClient(Config.ENDPOINT, credential)

    card_info = document_Client.begin_analyze_document(
        "prebuilt-creditCard", AnalyzeDocumentRquest(url_souce=card_url))
    result = card_info.result()

for document in result.documents:
        fields = document.get('fields', {})

        return {
            "card_name": fields.get('CardHolderName', {})get('content'),
            "card_number": fields.get('CardNumber', {})get('content'),
            "expiry_date": fields.get('ExpirationDate', {})get('content'),
            "card_name": fields.get('IssuingBank', {})get('content'),
        }    


        return result
    except Exception as ex:
        return None
