# Python Hello World Flask Application

A simple Flask web application that demonstrates basic web service functionality with health checks and metrics endpoints.

## Features

- **Hello World Endpoint**: Returns a simple greeting message
- **Health Check**: `/status` endpoint for monitoring application health
- **Metrics**: `/metrics` endpoint providing application metrics
- **Docker Support**: Containerized application with optimized Dockerfile
- **Testing**: Comprehensive test suite using pytest
- **Logging**: Application logging to file

## Endpoints

- `GET /` - Returns "Hello World!" message
- `GET /status` - Health check endpoint
- `GET /metrics` - Application metrics endpoint

## Requirements

- Python 3.8+
- Flask 1.1.4
- Werkzeug 1.0.1

## Installation

1. Clone the repository:
```bash
git clone https://github.com/khalidfarig1/python-heloworld2.git
cd python-heloworld2
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Local Development

```bash
python app.py
```

The application will be available at `http://localhost:5000`

### Using Docker

```bash
# Build the image
docker build -t python-heloworld2 .

# Run the container
docker run -p 5000:5000 python-heloworld2
```

## Testing

Run the test suite using pytest:

```bash
pip install pytest
pytest test_with_pytest.py -v
```

## API Documentation

### GET /

Returns a simple greeting message.

**Response:**
```
Hello World!
```

### GET /status

Health check endpoint for monitoring.

**Response:**
```json
{
  "result": "OK - healthy"
}
```

### GET /metrics

Application metrics endpoint.

**Response:**
```json
{
  "status": "success",
  "code": 0,
  "data": {
    "UserCount": 140,
    "UserCountActive": 23
  }
}
```

## Docker Features

- Multi-stage build for optimized image size
- Non-root user for security
- Health check integration
- Proper environment variable handling
- Logging configuration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).
