FROM python:3.9-slim
COPY . /app
WORKDIR /app

ENV PATH_EXTRACT_TEXT "/app"

# Install dependencies
RUN pip install opencv-python pytesseract tesseract flask 
EXPOSE 4005

ENTRYPOINT [ "python" ]
CMD [ "extract.py" ]
