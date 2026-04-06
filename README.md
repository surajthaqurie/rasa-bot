# Rasa Chatbot

A specialized Point of Sale conversational assistant built with **Rasa**.

## Setup & Installation

1. **Configure Environment:**
   Copy the sample environment file and update your variables:
   ```bash
   cp .env.sample .env
   ```

2. **Build the Project:**
   This will install dependencies and train the initial model (via the Docker image):
   ```bash
   make build
   ```

3. **Run the Assistant:**
   ```bash
   make run
   ```
   *The assistant will be available at http://localhost:5005.*

## Testing & Documentation

### 1. Interactive Swagger UI
The easiest way to test the API is through the built-in Swagger interface:
- **URL**: `http://localhost:5005/webhooks/conversation/swagger`
- **Use**: Click "Try it out", enter your message, and click "Execute".

### 2. Manual Terminal Testing (cURL)
```bash
curl -X POST http://localhost:5005/webhooks/conversation/ \
     -H "Authorization: Bearer YOUR_RASA_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{
           "sender": "user123",
           "message": "hello"
         }'
```

**Standardized Response Signature:**
```json
{
  "message": "success",
  "success": true,
  "data": {
    "message": {
      "recipient_id": "user123",
      "text": "Namaste! How can I help you today?"
    }
  }
}
```

## Developer Tools

### Run Automated Tests
Verify that the bot's logic is correct by running the test stories:
```bash
make test
```

### Visualize Conversations
Generate a graph to see all possible conversation paths:
```bash
make visualize
```

### Manual Shell Interaction
Talk to the bot directly in your terminal:
```bash
make shell
```

---
> [!NOTE]
> All configurations (Database, Ports, Tokens) are managed in the .env file.
