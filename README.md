# Todo API

A simple RESTful API built using Flask for managing Todo items with CRUD operations.

## API Endpoints

### 1. Create a Todo Item

**Endpoint:** `POST /items`

**Request Body:**

```json
{
  "title": "My Task",
  "task": "Complete the assignment",
  "date": "2026-04-01"
}
```

**Response:**

```json
{
  "message": "item added lol"
}
```

---

### 2. Get All Todo Items

**Endpoint:** `GET /items`

**Response:**

```json
[
  {
    "id": 1,
    "title": "My Task",
    "task": "Complete the assignment",
    "date": "2026-04-01",
    "done": false
  }
]
```

---

### 3. Update a Todo Item

**Endpoint:** `PUT /items/{id}`

**Request Body:**

```json
{
  "task": "Updated task",
  "done": true
}
```

**Response:**

```json
{
  "message": "updated with success"
}
```

---

### 4. Delete a Todo Item

**Endpoint:** `DELETE /items/{id}`

**Response:**

```json
{
  "message": "deleted with successfully"
}
```
