# DevPost API
An unofficial, scrape-based API for DevPost

![DroneCI](https://img.shields.io/drone/build/ViRb3/devpost-api)
![Docker Pulls](https://img.shields.io/docker/pulls/virb3/devpost-api)
![Size](https://img.shields.io/github/repo-size/ViRb3/devpost-api)
![GitHub Activity](https://img.shields.io/github/last-commit/ViRb3/devpost-api)
![License](https://img.shields.io/github/license/ViRb3/devpost-api)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/ViRb3/devpost-api.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/ViRb3/devpost-api/alerts/)

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

## To-do
### Remaining endpoints
### Performance
- Async HTTP ([httpx?](https://github.com/encode/httpx))
- Parallelize

## Running
### Docker (recommended)
- `docker pull virb3/devpost-api:latest`
- `docker run virb3/devpost-api:latest -p 5000`
- You can access the API at `http://127.0.0.1:5000`
### Development
- `pipenv install lxml` (or use prebuilt Linux package)
- `pipenv run python main.py`

## License
### [MIT](LICENSE)