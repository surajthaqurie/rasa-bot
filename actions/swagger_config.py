import os
import logging

logger = logging.getLogger(__name__)

# OpenAPI 3.0 Specification
OPENAPI_SPEC = {
    "openapi": "3.0.0",
    "info": {
        "title": "Rasa Chatbot API",
        "description": "Interactive API for the Rasa Chatbot",
        "version": "1.0.0"
    },
    "paths": {
        "/webhooks/conversation/": {
            "post": {
                "summary": "Send a message to the chatbot",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "sender": {"type": "string", "example": "user123"},
                                    "message": {"type": "string", "example": "hello"},
                                    "metadata": {"type": "object"}
                                },
                                "required": ["sender", "message"]
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "Bot Message Object",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "message": {"type": "string", "example": "success"},
                                        "success": {"type": "boolean", "example": True},
                                        "data": {
                                            "type": "object",
                                            "properties": {
                                                "message": {
                                                    "type": "object",
                                                    "properties": {
                                                        "recipient_id": {"type": "string"},
                                                        "text": {"type": "string"}
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    },
    "components": {
        "securitySchemes": {
            "bearerAuth": {
                "type": "http",
                "scheme": "bearer"
            }
        }
    },
    "security": [{"bearerAuth": []}]
}

def get_swagger_html() -> str:
    """Loads the Swagger UI HTML template from a separate file."""
    try:
        filepath = os.path.join(os.path.dirname(__file__), "swagger.html")
        with open(filepath, "r") as f:
            return f.read()
    except Exception as e:
        logger.error(f"Failed to load Swagger UI template: {e}")
        return "<h1>Documentation Unavailable</h1>"
