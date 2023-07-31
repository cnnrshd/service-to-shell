FROM python:3.11-slim
# Make a directory /app
RUN mkdir /app
# Expose port 8000
EXPOSE 8000
# Set the working directory to /app
WORKDIR /app
# Install required system packages (nslookup)
RUN apt-get update && apt-get install -y dnsutils
# Copy the current directory contents into the container at /app
COPY ./requirements.txt /app/requirements.txt
# Install any needed packages specified in requirements.txt
RUN pip install -r /app/requirements.txt
# Copy the app
COPY ./main.py /app/main.py
# Run main.py when the container launches
CMD ["uvicorn", "main:app", "--header", "server:dnssearcher v0.1.0", "--host", "", "--port", "8000"]