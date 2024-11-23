# Flask Application with Redis and Docker

This project demonstrates a Flask web application integrated with Redis for visitor counting and random quote generation. The application is containerized using Docker, with sensitive variables like the Redis password managed securely via environment variables.

---

## Features

- Flask app with dynamic visitor count and motivational quotes.
- Redis backend for storing visitor counts.
- Environment variable support for sensitive information like the Redis password.
- Docker Compose setup for multi-service orchestration.

---

## Prerequisites

1. Install Docker and Docker Compose.
2. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

---

## Project Structure

```
.
├── app.py                # Flask application
├── Dockerfile            # Multistage Docker build file
├── docker-compose.yml    # Docker Compose configuration
├── .env                  # Environment variables file (ignored by Git)
└── .gitignore            # Git ignore file
```

---

## Setup Instructions

### 1. Create the `.env` file

Create a `.env` file in the project root with the following content:

```env
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_PASSWORD=your_secure_password
```

- Replace `your_secure_password` with a strong, secure password for Redis.

### 2. Build and Run the Application

Build and start the application using Docker Compose:

```bash
docker-compose up --build
```

This command:
- Builds the Docker image for the Flask app.
- Starts both the Flask app (`web`) and the Redis service.

---

## Environment Variables

The application uses the following environment variables, which are defined in the `.env` file:

| Variable         | Description                 | Default Value |
|------------------|-----------------------------|---------------|
| `REDIS_HOST`     | Hostname of the Redis server| `redis`       |
| `REDIS_PORT`     | Port number for Redis       | `6379`        |
| `REDIS_PASSWORD` | Password for Redis          | -             |

---

## Access the Application

1. Open your browser and navigate to: [http://localhost:7777](http://localhost:7777)
2. To see quotes and visit counts, click the button or refresh the `/count` endpoint.

---

## Stopping the Application

To stop the application and remove all containers:

```bash
docker-compose down
```

---

## Security Notes

1. The `.env` file is included in `.gitignore` to prevent sensitive data from being pushed to version control.
2. Always use a strong password for `REDIS_PASSWORD` to secure your Redis instance.

---

