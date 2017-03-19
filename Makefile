
# Self-Documented Makefile
# http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help
help: ## Show this help message.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

check_dead_links: ## Run awesome_bot to check for dead links in README.md
	awesome_bot -t5 --allow-dupe --allow-redirect --allow-timeout README.md

toc: ## Generate table of contents for README
	doctoc --maxlevel 3 README.md

