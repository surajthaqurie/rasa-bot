import logging
from sanic import Blueprint, response
from rasa.core.channels.channel import InputChannel, UserMessage, CollectingOutputChannel
from typing import Text, Callable, Any, Dict, List

# Import modular Swagger configuration
from .swagger_config import OPENAPI_SPEC, get_swagger_html

logger = logging.getLogger(__name__)

class ChatConnector(InputChannel):
    """
    Standardized Native Rasa connector for Production.
    Provides a professional /webhooks/conversation/ endpoint with a custom response signature.
    Features: Standardized JSON output, Health monitoring, and Interactive Swagger UI.
    """

    @classmethod
    def name(cls) -> Text:
        # This will make the URL: /webhooks/conversation/
        return "conversation"

    def blueprint(self, on_new_message: Callable[[UserMessage], Any]) -> Blueprint:
        custom_webhook = Blueprint("custom_webhook", __name__)

        @custom_webhook.route("/health", methods=["GET"])
        async def health(request):
            """Endpoint for uptime monitoring."""
            return response.json({"status": "ok", "message": "success", "success": True})

        @custom_webhook.route("/openapi.json", methods=["GET"])
        async def openapi(request):
            """Returns the OpenAPI 3.0 specification for the Chat API from the modular config."""
            return response.json(OPENAPI_SPEC)

        @custom_webhook.route("/swagger", methods=["GET"])
        async def swagger(request):
            """Serves the interactive Swagger UI using a separate HTML template."""
            return response.html(get_swagger_html())

        @custom_webhook.route("/status", methods=["GET"])
        async def status(request):
            """Endpoint for detailed server status information."""
            return response.json({
                "message": "success",
                "success": True,
                "data": {
                    "status": "ready",
                    "connector": "native_conversation",
                    "api_path": "/webhooks/conversation/"
                }
            })

        @custom_webhook.route("/", methods=["POST"])
        async def receive(request):
            """Main chat endpoint with a standardized Production response signature."""
            sender_id = request.json.get("sender")
            text = request.json.get("message")
            
            if not sender_id or not text:
                return response.json({
                    "message": "sender and message are required",
                    "success": False,
                    "data": None
                }, status=400)

            collector = CollectingOutputChannel()
            
            try:
                await on_new_message(
                    UserMessage(
                        text,
                        collector,
                        sender_id,
                        input_channel=self.name(),
                        metadata=request.json.get("metadata")
                    )
                )
            except Exception as e:
                logger.error(f"Error in conversation connector: {e}")
                return response.json({
                    "message": f"Inner Error: {str(e)}",
                    "success": False,
                    "data": None
                }, status=500)

            # Standardized Production Response Signature (Single Object)
            first_msg = collector.messages[0] if collector.messages else {}
            
            return response.json({
                "message": "success",
                "success": True,
                "data": {
                    "message": first_msg
                }
            })

        return custom_webhook
