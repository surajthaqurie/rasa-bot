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

The server uses a **Custom Native Connector** to provide clean and standardized endpoints on port `5005`.

### 1. Check Server Status
```bash
curl http://localhost:5005/status
```

### 2. Chat with the Bot
```bash
curl -X POST http://localhost:5005/webhook/conversation \
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
