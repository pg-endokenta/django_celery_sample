.PHONY: dev-build
dev-build:
	docker compose -f compose.yml build

.PHONY: dev-up-d
dev-up-d:
	docker compose -f compose.yml up -d

.PHONY: dev
dev:
	@make dev-build
	@make dev-up-d

.PHONY: down
down:
	docker compose -f compose.yml down
