# API Specification (MVP)

## Authentication

### POST /auth/register
- Registers a new user
- Input:
  - email
  - password
- Response:
  - success message

### POST /auth/login
- Authenticates a user
- Input:
  - email
  - password
- Response:
  - access token (future)

---

## Transactions

### POST /transactions
- Add income or expense
- Requires authentication
- Input:
  - amount
  - type (income/expense)
  - category
  - date
  - note (optional)

### GET /transactions
- Fetches all transactions for the logged-in user

---

## Insights

### GET /insights/monthly
- Returns monthly spending summary

## Health

### GET /health
- API health check
