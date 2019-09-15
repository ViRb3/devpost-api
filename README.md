# DevPost API
An unofficial, scrape-based API for DevPost

![DroneCI](https://img.shields.io/drone/build/ViRb3/devpost-api)
![Docker Pulls](https://img.shields.io/docker/pulls/virb3/devpost-api)
![GitHub Activity](https://img.shields.io/github/last-commit/ViRb3/devpost-api)
![License](https://img.shields.io/github/license/ViRb3/devpost-api)

## Usage
```
/user/<username>
/project/<project_name>
```

## To-do
### Endpoints
| Profile       | Project           | Hackathon
| ---           | ---               | ---
| Extra links   | Picture           | Everything
| Cover image   | Updates
|               | Text formatting
|               | Likes
|               | Comments
### Performance
- Async HTTP ([httpx?](https://github.com/encode/httpx))
- Parallelize

## Running
### Development
`pipenv run python main.py`
### Deployment (Linux only)
`pipenv run gunicorn --bind 0.0.0.0:5000 wsgi:app`

## [License](LICENSE)