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

## Testing & Shell

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

## API Connection

To connect an external application to the Rasa server, use the REST API with the Authorization header.

### 1. Check Version
```bash
curl -H "Authorization: Bearer YOUR_RASA_TOKEN" http://localhost:5005/version
```

### 2. Chat with the Bot
```bash
curl -X POST http://localhost:5005/webhooks/rest/webhook \
     -H "Authorization: Bearer YOUR_RASA_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{
           "sender": "user123",
           "message": "hello"
         }'
```

---
> [!NOTE]
> All configurations (Database, Ports, Tokens) are managed in the .env file.
