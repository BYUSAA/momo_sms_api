import xml.etree.ElementTree as ET
import json

def parse_xml(xml_path, json_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    transactions = []

    for sms in root.findall("sms"):
        transaction = {
            "id": sms.get("id"),
            "type": sms.get("type"),
            "amount": sms.get("amount"),
            "sender": sms.get("sender"),
            "receiver": sms.get("receiver"),
            "timestamp": sms.get("timestamp")
        }
        transactions.append(transaction)

    with open(json_path, "w") as f:
        json.dump(transactions, f, indent=4)

    return transactions


if __name__ == "__main__":
    parse_xml("data/modified_sms_v2.xml", "data/transactions.json")
