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
## Interactive API Documentation

Go to http://127.0.0.1:8000/docs.

## Alternative API Docuememtation

Now go to http://127.0.0.1:8000/redocs.

## To-do
### Remaining endpoints
### Performance
- [x] Async HTTP (Use[httpx](https://github.com/encode/httpx))
- Parallelize

## Running
### Development
`pipenv run uvicorn main:app --reload`
### Deployment (Linux only)
`pipenv run uvicorn main:app`
# [License](LICENSE)
