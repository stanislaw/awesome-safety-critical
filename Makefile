# Self-Documented Makefile
# http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help
help: ## Show this help message.
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

check_dead_links: ## Run awesome_bot to check for dead links in docs/index.rst
	python3 -m venv .venv && \
		. .venv/bin/activate && \
		pip install requests && \
		python3 link_health.py docs/source/index.rst

doc: ## Generate new awesome-safety-critical content
	cd docs && make clean html

