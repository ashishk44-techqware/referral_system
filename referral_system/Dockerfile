# Use the official Python image as a base image
FROM python:3.8.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /referral_system

# Install dependencies
RUN pip freeze
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the project files into the container
COPY . .

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]