# DevPost API
An unofficial, scrape-based API for DevPost

[![Build Status](https://travis-ci.org/ViRb3/devpost-api.svg?branch=master)](https://travis-ci.org/ViRb3/devpost-api)
![Docker Pulls](https://img.shields.io/docker/pulls/virb3/devpost-api)
![Size](https://img.shields.io/github/repo-size/ViRb3/devpost-api)
![GitHub Activity](https://img.shields.io/github/last-commit/ViRb3/devpost-api)
![License](https://img.shields.io/github/license/ViRb3/devpost-api)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/ViRb3/devpost-api.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/ViRb3/devpost-api/alerts/)

## Features
| Profile           | Project           | Event
| ---               | ---               | ---
| Names             | Title             |
| Bio               | Heading
| Profile image     | Text
| Links             | Built with
| Skills            | Submissions
| Interests         | Members
| Software entries  |
| Followers         |
| Following         |
| Likes             |

## API Endpoints
```
/user/:username
/project/:project_name
```

## [Docker image](https://hub.docker.com/r/virb3/devpost-api)
Supported architectures: `amd64`, `arm32v6`, `arm32v7`, `arm64v8`
- `docker pull virb3/devpost-api:latest`
- `docker run virb3/devpost-api:latest -p 5000`
- You can access the API at `http://127.0.0.1:5000`
## Development
- `pipenv install lxml` (or use prebuilt Linux package)
- `pipenv run python main.py`

## To-do
- Performance
  - Async HTTP ([httpx?](https://github.com/encode/httpx))
  - Parallelize
- Remaining endpoints

## License
### [MIT](LICENSE)