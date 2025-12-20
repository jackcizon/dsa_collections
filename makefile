.PHONY: all lint test coverage pre_commit commit changelog

# 默认任务：Lint + Test + Coverage
all: lint test coverage pre_commit changelog

# 使用 Ruff 替代 /black/flake8/pylint
lint:
	poetry run ruff check algo/ ds/ tests/
	poetry run ruff format algo/ ds/ tests/

# 运行 pytest
test:
	poetry run pytest -v

# 运行测试并生成覆盖率报告
coverage:
	poetry run coverage report -m
	poetry run coverage html

# pre-commit hook 检查
pre_commit:
	poetry run pre-commit run -a

# 使用 Commitizen 提交
commit:
	cz commit

# 生成 Changelog
changelog:
	cz changelog