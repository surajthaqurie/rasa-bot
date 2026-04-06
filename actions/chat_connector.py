import logging
from sanic import Blueprint, response
from rasa.core.channels.channel import InputChannel, UserMessage, CollectingOutputChannel
from typing import Text, Callable, Any, Dict, List

logger = logging.getLogger(__name__)

class ChatConnector(InputChannel):
    """A custom REST connector that provides a clean '/webhook/chat' endpoint."""

    @classmethod
    def name(cls) -> Text:
        return "chat"

    def blueprint(self, on_new_message: Callable[[UserMessage], Any]) -> Blueprint:
        custom_webhook = Blueprint("custom_webhook", __name__)

        @custom_webhook.route("/health", methods=["GET"])
        async def health(request):
            return response.json({"status": "ok"})

        @custom_webhook.route("/status", methods=["GET"])
        async def status(request):
            # This mimics the /version endpoint
            return response.json({
                "status": "ready",
                "connector": "custom_chat",
                "api_path": "/webhook/conversation"
            })

        @custom_webhook.route("/webhook/conversation", methods=["POST"])
        async def receive(request):
            sender_id = request.json.get("sender")
            text = request.json.get("message")
            input_channel = self.name()

            collector = CollectingOutputChannel()
            
            try:
                await on_new_message(
                    UserMessage(
                        text,
                        collector,
                        sender_id,
                        input_channel=input_channel,
                        metadata=request.json.get("metadata")
                    )
                )
            except Exception as e:
                logger.error(f"Error in custom chat connector: {e}")
                return response.json({"error": str(e)}, status=500)

            return response.json(collector.messages)

        return custom_webhook
