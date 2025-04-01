FROM rayproject/ray:latest

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy application code (if needed)
COPY ./app /app

# Setup startup script
COPY ./start.sh .
