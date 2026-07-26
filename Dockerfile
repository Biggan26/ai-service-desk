FROM python:3.12-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1

# Working directory
WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Create non-root user
RUN addgroup --system app && \
    adduser --system --ingroup app --home /home/app app

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies into .venv
RUN uv sync --frozen --no-dev

# Copy application source
COPY --chown=app:app app ./app

# Copy environment file (optional)
COPY --chown=app:app .env ./

# Give ownership to app user
RUN chown -R app:app /app

# Use virtual environment by default
ENV PATH="/app/.venv/bin:$PATH"

# Switch to non-root user
USER app

# Expose application port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=2)"

# Start FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
