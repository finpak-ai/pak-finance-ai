# System Architecture

Pak Finance AI is a simple web-based personal finance application.

## High-Level Overview

The system is divided into four main components:

1. Frontend (Web Interface)
2. Backend (API Server)
3. Database
4. AI Module

Each component has a clear responsibility and communicates through well-defined APIs.

---

## Frontend

**Purpose:**
- Provides user interface for the application
- Allows users to log in, add transactions, and view summaries

**Technologies (MVP):**
- HTML
- CSS
- JavaScript

The frontend communicates with the backend using HTTP API requests.

---

## Backend

**Purpose:**
- Handles business logic
- Manages users and authentication
- Processes financial data

**Technologies:**
- Python
- FastAPI

The backend exposes REST APIs used by the frontend.

---

## Database

**Purpose:**
- Stores user data
- Stores transactions and budgets

**Technologies:**
- PostgreSQL (SQLite during development)

Each user’s data is separated using a unique user ID.

---

## AI Module

**Purpose:**
- Analyzes spending patterns
- Generates financial insights and suggestions

**Technologies (initial):**
- Rule-based logic
- Python

Advanced ML models will be added in later phases.
