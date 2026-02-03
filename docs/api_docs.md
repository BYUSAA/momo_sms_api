# MoMo SMS API Documentation

## Authentication
Basic Authentication required.

Username: admin  
Password: password123  

---

## GET /transactions
Returns all SMS transactions.

Response:
200 OK

---

## GET /transactions/{id}
Returns a single transaction.

Errors:
404 Not Found

---

## POST /transactions
Creates a new transaction.

Response:
201 Created

---

## PUT /transactions/{id}
Updates an existing transaction.

Response:
200 OK

---

## DELETE /transactions/{id}
Deletes a transaction.

Response:
200 OK

---

## Security Note
Basic Authentication is weak because credentials are sent with every request.
JWT or OAuth2 should be used for production systems.
