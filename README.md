# Yet Another Expense Tracker

Yet Another Expense Tracker is yet another expense tracker built with Django to fulfill my specific use case.

It is also for trying out Heroku free tier to see if I need to host it on my own server...

Obviously there is many other frameworks and languages that I can explore but I'm already knee deep in Django which is more than enough for to quickly create this expense tracker app.

## Getting Started

This project uses both Docker and Docker Compose. Refer to https://docs.docker.com/compose/install/

Last tested in WSL2 Ubuntu 20.04. Should work with Docker for Desktop on Windows and macOS but no guarantee. 

## Build

```shell
# Make sure you're at project root path containing both Dockerfile and docker-compose.yml
$ docker-compose build
```

## Troubleshooting

1. Use `sudo chown -R $USER:$USER .` at the root project folder when extending new Django app as any files created in Docker are owned by `root` user by default.

## Deployment

```shell
# Running in detached mode 
$ docker-compose up -d

# Tail and follow the log from the last 100 lines
$ docker-compose logs -f --tail 100
```
