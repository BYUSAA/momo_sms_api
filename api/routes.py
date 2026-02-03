from http.server import BaseHTTPRequestHandler
import json
from api.auth import is_authenticated

DATA_FILE = "data/transactions.json"


def load_transactions():
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_transactions(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


class RequestHandler(BaseHTTPRequestHandler):

    def _unauthorized(self):
        self.send_response(401)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"error": "Unauthorized"}).encode())

    def _not_found(self):
        self.send_response(404)
        self.end_headers()

    def authenticate(self):
        if not is_authenticated(self.headers):
            self._unauthorized()
            return False
        return True

    def do_GET(self):
        if not self.authenticate():
            return

        transactions = load_transactions()
        parts = self.path.strip("/").split("/")

        if self.path == "/transactions":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(transactions).encode())

        elif len(parts) == 2 and parts[0] == "transactions":
            tx_id = parts[1]
            for tx in transactions:
                if tx["id"] == tx_id:
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(json.dumps(tx).encode())
                    return
            self._not_found()

    def do_POST(self):
        if not self.authenticate():
            return

        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)
        new_transaction = json.loads(body)

        transactions = load_transactions()
        transactions.append(new_transaction)
        save_transactions(transactions)

        self.send_response(201)
        self.end_headers()

    def do_PUT(self):
        if not self.authenticate():
            return

        parts = self.path.strip("/").split("/")
        if len(parts) != 2:
            self._not_found()
            return

        tx_id = parts[1]
        content_length = int(self.headers.get("Content-Length", 0))
        updated_transaction = json.loads(self.rfile.read(content_length))

        transactions = load_transactions()
        for i, tx in enumerate(transactions):
            if tx["id"] == tx_id:
                transactions[i] = updated_transaction
                save_transactions(transactions)
                self.send_response(200)
                self.end_headers()
                return

        self._not_found()

    def do_DELETE(self):
        if not self.authenticate():
            return

        parts = self.path.strip("/").split("/")
        if len(parts) != 2:
            self._not_found()
            return

        tx_id = parts[1]
        transactions = load_transactions()
        new_transactions = [tx for tx in transactions if tx["id"] != tx_id]

        save_transactions(new_transactions)
        self.send_response(200)
        self.end_headers()
