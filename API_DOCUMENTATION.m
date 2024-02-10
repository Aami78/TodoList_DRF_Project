# ToDo List API Documentation

In this documentation, you will find detailed information on how to set up and use the ToDo List API built using Django REST Framework. The API allows users to perform CRUD operations on ToDo items, manage user authentication, and access various endpoints for registration, login, logout, and ToDo item management.

## Authentication

The API uses token-based authentication. Users need to obtain a token by logging in using their username and password. This token must be included in the Authorization header of subsequent requests to access protected endpoints.

### Register

- **Endpoint:** `/register/`
- **Method:** POST
- **Data:** `username`, `password`
- **Response:** A token, user ID, and username.

### Login

- **Endpoint:** `/login/`
- **Method:** POST
- **Data:** `username`, `password`
- **Response:** A token, user ID, and username.

After obtaining your token, include it in the Authorization header as follows:

- ** Authorization: Token <your_token_here>


## ToDo Item Endpoints

Here's how you can manage your ToDo items:

### List/Create ToDo Items

#### List Endpoint

- **Endpoint:** `/todos/`
- **Method:** GET
- **Headers:** `Authorization: Token <your_token_here>`
- **Response:** A list of ToDo items associated with the authenticated user.

#### Create Endpoint

- **Endpoint:** `/todos/`
- **Method:** POST
- **Headers:** `Authorization: Token <your_token_here>`
- **Data:** `title`, `description` (optional), `completed` (optional, default is false)
- **Response:** The created ToDo item.

### Retrieve/Update/Delete a ToDo Item

#### Retrieve Endpoint

- **Endpoint:** `/todos/<int:id>/`
- **Method:** GET
- **Headers:** `Authorization: Token <your_token_here>`
- **Response:** The requested ToDo item.

#### Update Endpoint

- **Endpoint:** `/todos/<int:id>/`
- **Method:** PUT or PATCH
- **Headers:** `Authorization: Token <your_token_here>`
- **Data:** Any of `title`, `description`, `completed`
- **Response:** The updated ToDo item.

#### Delete Endpoint

- **Endpoint:** `/todos/<int:id>/`
- **Method:** DELETE
- **Headers:** `Authorization: Token <your_token_here>`
- **Response:** A confirmation that the ToDo item has been deleted.

## Filtering and Sorting

You can filter and sort the list of ToDo items by appending query parameters to the GET request URL:

- Filter by Completion: `/todos/?completed=true` or `/todos/?completed=false`
- Sort by Creation Date: `/todos/?ordering=created_at` for ascending order or `/todos/?ordering=-created_at` for descending order.

## Examples

Here are a few examples of how to use the API endpoints:

### Create Todo Item

- **URL**: `/api/todos/`
- **Method**: `POST`
- **Body**:

```json
{
  "title": "Buy milk",
  "description": "Remember to check expiration dates."
}

## Response:

{
  "id": 1,
  "title": "Buy milk",
  "description": "Remember to check expiration dates.",
  "completed": false
}


#Conclusion
This document covers the basics of interacting with the ToDo List Application API. With the information provided, you should be able to effectively manage your ToDo items through our API.