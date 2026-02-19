# Building and Securing a REST API for MoMo SMS Transactions

## Project Overview
This project implements a **secure REST API** for managing Mobile Money (MoMo) SMS transactions. It parses SMS data from an XML dataset, converts it into JSON, and exposes it via a **RESTful API** built using **plain Python (`http.server`)**.

The API supports **full CRUD operations** (Create, Read, Update, Delete) and is protected using **Basic Authentication**. The project also integrates **Data Structures and Algorithms (DSA)** to demonstrate efficient search techniques and compare performance between linear search and dictionary-based lookup.

This system is designed to provide **real-world experience** in API design, authentication, data processing, and algorithmic optimization.

---

## Team Ownership
**Team Eight**
_____________________________________________________________________
| Member                  | Role                                    |
|-------------------------|-----------------------------------------|
| James Giir Deng         | Team Lead & Backend Developer           |
| Byusa M Martin De Poles | Frontend Developer & Database Architect |
_____________________________________________________________________

All members actively contributed to **design, development, testing, and documentation** of this project.

---

## Technologies Used
- Python 3  
- `http.server` for REST API  
- XML & JSON data processing  
- Basic Authentication  
- Linear Search & Dictionary Lookup  
- Postman / curl for API testing

---

## Project Structure
```
momo_sms_api/
├── api/                  # REST API scripts
│   ├── server.py         # Entry point
│   ├── auth.py           # Authentication logic
│   └── routes.py         # CRUD endpoints
├── dsa/                  # Data parsing and DSA scripts
│   ├── parser.py         # XML to JSON conversion
│   ├── search.py         # Linear & dictionary search
│   └── performance.py    # Performance comparison
├── data/                 # Dataset
│   ├── modified_sms_v2.xml
│   └── transactions.json
├── docs/                 # API documentation
│   └── api_docs.md
├── screenshots/          # Test screenshots
│   └── *.txt / *.png
└── README.md             # Project README
```

---

## Setup Instructions

### 1. Parse XML to JSON
```bash
python dsa/parser.py
```
This converts `modified_sms_v2.xml` into `transactions.json`.

### 2. Start the API Server
```bash
python api/server.py
```
The server runs at: `http://localhost:8000`

---

## Authentication
All endpoints require **Basic Authentication**.

**Credentials:**
- Username: `admin`
- Password: `password123`

Unauthorized requests return:
```
401 Unauthorized
```

> ⚠️ Note: Basic Authentication is suitable for learning but not recommended for production. JWT or OAuth2 are more secure alternatives.

---

## API Endpoints

__________________________________________________________________
| Method | Endpoint           | Description                      |
|--------|--------------------|----------------------------------| 
| GET    | /transactions      | Get all transactions             |
| GET    | /transactions/{id} | Get a specific transaction by ID |
| POST   | /transactions      | Add a new transaction            |
| PUT    | /transactions/{id} | Update an existing transaction   |
| DELETE | /transactions/{id} | Delete a transaction             |
__________________________________________________________________

All requests must include valid authentication headers.

---

## Data Structures & Algorithms (DSA)

### Linear Search
- Iterates through the list of transactions  
- **Time Complexity:** O(n)

### Dictionary Lookup
- Maps ID → transaction for direct access  
- **Time Complexity:** O(1) average case

### Performance Comparison
The `performance.py` script compares execution times for **linear search** and **dictionary lookup**, demonstrating the efficiency of hash-based structures for fast retrieval in large datasets.

---

## Security Considerations
- **Basic Authentication** is simple but insecure for production: credentials are sent with every request.  
- For production systems, consider:  
  - **JWT (JSON Web Tokens)** for stateless authentication  
  - **OAuth2** for secure authorization

---

## Testing
Endpoints were tested using **Postman** and **curl**.  
Screenshots of tests (GET, POST, PUT, DELETE, and Unauthorized requests) are included in the `screenshots/` folder.

---

## Conclusion
This project demonstrates:
- Practical API development using Python  
- Securing endpoints with authentication  
- Efficient data retrieval with DSA techniques  
- Documentation and testing best practices

It is suitable for academic submission, portfolio demonstration, and learning real-world API design.

---

## License
Academic use only.

---

## Authors / Team
- **James Giir Deng** – Team Lead & Backend Developer  
- **Byusa M Martin De Poles** – Frontend Developer & Database Architect  
**Team five**
