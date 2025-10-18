FROM python:3.11-slim

WORKDIR /app

# system deps (if needed for pandas/plotly; adjust if your base image already covers these)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV PORT=8050
EXPOSE 8050

# Use gunicorn in production; we exposed `server = app.server` in dashboard.py
CMD ["gunicorn", "-b", "0.0.0.0:8050", "dashboard:server", "--workers", "4", "--threads", "2"]
