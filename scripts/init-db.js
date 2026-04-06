/**
 * Rasa Chatbot - Database Initialization
 * Sets up a TTL (Time-To-Live) index for automatic conversation pruning.
 * Data retention: 14 days (1,209,600 seconds)
 */

// Target the 'rasa' database
db = db.getSiblingDB('rasa');

print("Setting up Data Retention Policy (14 days)...");

// Create the TTL index on latest_event_time
db.conversations.createIndex(
  { "latest_event_time": 1 },
  { 
    expireAfterSeconds: 1209600,
    name: "conversation_retention_ttl"
  }
);

print("Success: TTL Index 'conversation_retention_ttl' created on 'conversations' collection.");
