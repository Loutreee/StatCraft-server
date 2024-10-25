# Use an official Python runtime as a parent image
FROM python:3.9-slim AS base

# Set the working directory in the container
WORKDIR /app


# Make port 8501 available to the world outside this container
EXPOSE 8501

# Define environment variable
ENV NAME World

FROM base AS prod

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Lancer Streamlit avec app.py lorsque le conteneur démarre
CMD ["streamlit", "run", "StatCraft-server.py", "--server.port=8501", "--server.enableCORS=false", "--server.enableXsrfProtection=false"]

FROM base AS dev
CMD pip install -r requirements.txt && streamlit run StatCraft-server.py --server.port=8501 --server.enableCORS=false --server.enableXsrfProtection=false --server.runOnSave=true

# CMD ["pip","install" ,"--no-cache-dir", "-r requirements.txt;","streamlit", "run", "StatCraft-server.py", "--server.port=8501", "--server.enableCORS=false", "--server.enableXsrfProtection=false", "--server.runOnSave=true"]
