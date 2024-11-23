FROM python:3.8 AS build

WORKDIR /app

COPY ./app.py .

RUN pip install redis flask python-dotenv --target=/dependencies

FROM python:3.8-slim

WORKDIR /app

COPY --from=build /app/app.py .

COPY --from=build /dependencies /dependencies

ENV PYTHONPATH=/dependencies

EXPOSE 7777

CMD ["python", "app.py"]