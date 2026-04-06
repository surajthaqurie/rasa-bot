# #############################################################################
# # Rasa Chatbot - Automation Makefile
# # This file provides shortcuts for common developer tasks such as 
# # training the model, running the services, and performing tests.
# # #############################################################################
# Rasa Chatbot Makefile

.PHONY: help validate train run shell test visualize clean

help:
	@echo "Available commands:"
	@echo "  make validate    - Verify required .env variables are set"
	@echo "  make train       - Train the Rasa model"
	@echo "  make build       - Build Docker images"
	@echo "  make run         - Run Rasa and Action services"
	@echo "  make shell       - Open Rasa shell in the running container"
	@echo "  make test        - Run Rasa test stories"
	@echo "  make visualize   - Visualize conversation graph"
	@echo "  make clean       - Remove models and .rasa cache"

validate:
	@chmod +x scripts/validate_env.sh
	@./scripts/validate_env.sh

build:
	docker-compose build

train: validate
	docker-compose run --rm -e PYTHONWARNINGS=ignore rasa train

run: validate
	docker-compose up --build

shell: validate
	docker-compose exec rasa shell

test: validate
	docker-compose run --rm -e PYTHONWARNINGS=ignore rasa test

visualize:
	docker-compose run --rm -e PYTHONWARNINGS=ignore rasa visualize

clean:
	@echo "Cleaning up models, cache, and hidden configuration directories..."
	rm -rf models/*.tar.gz
	rm -rf .rasa/
	rm -rf .config/
	rm -rf .keras/
