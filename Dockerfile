FROM python:3.12-slim

WORKDIR /app

# 安装 poetry
RUN pip install poetry

# 关闭虚拟环境（Docker 自己就是隔离）
RUN poetry config virtualenvs.create false

# 先复制依赖文件，利用缓存
COPY pyproject.toml poetry.lock ./

RUN poetry install --no-interaction --no-root  --with dev

# 再复制代码
COPY . .

# 默认命令（CI 会覆盖，但本地也能用）
CMD ["pytest", "-v"]
