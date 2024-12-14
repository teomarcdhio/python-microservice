# Use python base container
FROM python:3
# Set the workign directory
WORKDIR /usr/src/app
# Copy the requirements definition 
COPY requirements.txt ./
# Install dependecies
RUN pip install --no-cache-dir -r requirements.txt
# Copy the main python file/s
COPY main.py .
# Expose port 5000
EXPOSE 5000
# Set the cmd to run the app
ENTRYPOINT [ "python", "./main.py" ]