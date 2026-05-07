# Quote of the Day API 🐳

A simple REST API that serves motivational quotes, containerized with Docker.

## Run with Docker

```bash
docker build -t quote-api .
docker-compose up
```

## Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /` | API info |
| `GET /quote/today` | Same quote all day (based on date) |
| `GET /quote/random` | Random quote |
| `GET /quote/<id>` | Quote by ID |
| `GET /quotes` | All quotes |

## Test it

```bash
curl http://localhost:5001/quote/today
curl http://localhost:5001/quote/random
curl http://localhost:5001/quotes
```
