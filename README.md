# DevPost API
An unofficial, scrape-based API for DevPost

![DroneCI](https://img.shields.io/drone/build/ViRb3/devpost-api)
![Docker Pulls](https://img.shields.io/docker/pulls/virb3/devpost-api)
![GitHub Activity](https://img.shields.io/github/last-commit/ViRb3/devpost-api)
![License](https://img.shields.io/github/license/ViRb3/devpost-api)

## Implemented
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

## Usage
```
/user/:username
/project/:project_name
```

## Downloads
### [Docker image](https://hub.docker.com/r/virb3/devpost-api)

## To-do
### Remaining endpoints
### Performance
- Async HTTP ([httpx?](https://github.com/encode/httpx))
- Parallelize

## Running
### Development
`pipenv run python main.py`
### Deployment (Linux only)
`pipenv run gunicorn --bind 0.0.0.0:5000 wsgi:app`

## License
### [MIT](LICENSE)