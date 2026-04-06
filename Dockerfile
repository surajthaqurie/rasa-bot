# #############################################################################
# # Rasa Chatbot - Production Docker Image
# # #############################################################################

# Use the latest stable official Rasa 3.6 base image
FROM rasa/rasa:3.6.21

# Set working directory
WORKDIR /app

# Copy all project files
COPY . /app

# Switch to root to install optional dependencies
USER root

# Upgrade pip and install the latest build tools
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache/pip

# Pre-train the model to make the image truly self-sufficient
RUN rasa train --fixed-model-name model

# Switch back to non-root for security
USER 1001

# Production Defaults (Silencing non-actionable library internal warnings)
ENV RASA_TOKEN=""
ENV PYTHONWARNINGS="ignore"
ENV SQLALCHEMY_SILENCE_UBER_WARNING="1"
ENV PYTHONPATH="."

# Expose default Rasa port
EXPOSE 5005

# Set entrypoint to run validation first
ENTRYPOINT ["/app/scripts/entrypoint.sh"]

# Default command to run Rasa server
CMD ["run", "--enable-api", "--auth-token", "${RASA_TOKEN}", "--cors", "*", "--port", "5005", "--endpoints", "endpoints.yml"]