# #############################################################################
# # Rasa Chatbot - Production Docker Image
# # This file builds a customized Rasa image optimized for production, 
# # including all project dependencies and pre-trained model hooks.
# # #############################################################################
# Use official Rasa 3.6 base image
FROM rasa/rasa:3.6.0

# Set working directory
WORKDIR /app

# Copy all project files
COPY . /app

# Switch to root to install optional dependencies
USER root

# Upgrade pip and install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache/pip

# Switch back to non-root for security
USER 1001

# Default environment variables
ENV RASA_TOKEN=""

# Expose default Rasa port
EXPOSE 5005

# Set entrypoint to run validation first
ENTRYPOINT ["/app/scripts/entrypoint.sh"]

# Default command to run Rasa server with authentication enabled
CMD ["run", "--enable-api", "--auth-token", "${RASA_TOKEN}", "--cors", "*", "--port", "5005", "--endpoints", "endpoints.yml"]