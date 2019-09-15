# DevPost API
An unofficial, scrape-based API for DevPost

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