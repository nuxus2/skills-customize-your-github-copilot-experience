# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using FastAPI by defining endpoints, handling request data, and returning JSON responses.

## 📝 Tasks

### 🛠️ Project Setup and Endpoint Definition

#### Description
Set up a FastAPI project and create the first API endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Install and import `fastapi` and `uvicorn`
- Create a FastAPI application instance
- Define a GET endpoint at `/` that returns a JSON welcome message
- Run the app with `uvicorn` so the endpoint is accessible

### 🛠️ Data Models and Request Validation

#### Description
Define a data model for a resource and use request validation for incoming JSON payloads.

#### Requirements
Completed program should:

- Create a Pydantic model for a resource such as `Item` with fields like `id`, `name`, and `price`
- Define a POST endpoint at `/items/` that accepts an `Item` payload
- Validate incoming data and return the created item in the response

### 🛠️ CRUD Operations and Error Handling

#### Description
Add endpoints for reading, updating, and deleting resources, and handle missing resources gracefully.

#### Requirements
Completed program should:

- Define GET, PUT, and DELETE endpoints for item management
- Store items in a simple in-memory list or dictionary
- Return appropriate JSON responses for success and not-found cases
- Include error handling for requests to non-existent items