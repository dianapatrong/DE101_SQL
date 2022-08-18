# Lab 1: Docker for Databases

### Prerequisites
* [Install docker](https://docs.docker.com/engine/install/) 
* [Install pgAdmin](https://www.pgadmin.org/download/)
* Install docker compose (only if you are on Linux)

> NOTE: On desktop systems, such as Docker Desktop for Mac and Windows, docker compose is already included. 
> No additional steps are needed. 

### What You Will Learn
You'll learn how to:
* Read a docker-compose.yml file with a database service 
* Create a postgres database in a docker container
* Connect to PostgreSQL database running inside the container using a client (pgAdmin)
* Connect to PostgreSQL database running inside the container using the command line 

## Let's get started

### Docker Compose
In this folder there's a pre-defined [`docker-compose.yml`](docker-compose.yml) file, let's walk through the file
to make sure you understand it. 

```dockerfile
version: "3"
services:
    db:
        container_name: my_first_dockerized_db
        image: postgres:14-alpine
        ports:
            - "32007:3306"
        environment:
            - "POSTGRES_PASSWORD=${POSTGRES_PASSWORD}"
```

There are multiple clauses and keywords within this file: 
* `version`: This specifies the version of docker compose, in this case we are using version 3, and Docker will provide the appropriate features for this version. 
* `services`: This section defines all the containers that can be created, in this lab we will only have one database service.
* `container_name`: specifies a custom container name, rather than a generated default name
* `image`: Is used to mention the image name from which container will spin-up from. Image can be in the local system or hosted on some remote repository. 
* `ports`: This is used to map the container’s ports to the host machine `host port 32003: container port 5432`
* `environment`: Defines the environment variables set in the container

> NOTE: **Why do we need port mapping?** 
>
> As a general rule, a port can only map to a single service or process on each host. 
> Imagine that you have multiple PostgreSQL containers on a single host. By default, 
> each PostgreSQL instance wants to bind to port 5432 as it is its default port, while you could manually modify each 
> container to bind the container's service to a unique host port, this quickly becomes a hassle at scale.
> Instead, Docker and other container managers make it easy to map ports between the host OS and the container


### Environment variables in compose 
If you have multiple environment variables, you can substitute them by adding them to a default environment variable file named 
`.env` which compose automatically looks for in the project directory, alternatively you can provide a path to your environment 
variables file using the `--env-file` command line option. 
 
For this lab, we have a [`.env`](.env) file defined within this directory. Each line in an `env` file must be in `VARIABLE=VALUE` format. 
Compose files use a Bash-like syntax `${VARIABLE}` to evaluate. 

**.env** file: 

```shell script
POSTGRES_PASSWORD=secret
```

**docker-compose.yml** file: 

```shell script
POSTGRES_PASSWORD: "${POSTGRES_PASSWORD}"
```

### Docker Compose commands

`docker-compose up`: This command does the work of the `docker-compose build` and `docker-compose run` commands. 
It builds the images if they are not located locally and starts the containers.

`docker-compose down`: This command is used to destroy all the containers/services run from the Docker Compose file.

### Running docker compose 

Now that we are all set, let's run our docker-compose file: 

```shell script
$ docker-compose up
```

Open another terminal window and make sure your container is running: 

```shell script
$ docker-compose ps
NAME                     COMMAND                  SERVICE             STATUS              PORTS
my_first_dockerized_db   "docker-entrypoint.s…"   db                  running             5432/tcp, 0.0.0.0:32007->3306/tcp
```

### Connect to the PostgreSQL database
Now that our container is running, we will connect to the PostgreSQL instance.

#### Using the CLI

The following command lets you connect to the PostgreSQL CLI running inside the Docker container.

```
$ docker-compose exec db bash
bash-5.1# 
```

Once the interactive terminal is started, you can connect to the PostgreSQL instance using the default user.

```
bash-5.1# psql -h localhost -U postgres
psql (14.5)
Type "help" for help.

postgres=# 
```

* `-h`: You need to provide the hostname on which the PostgreSQL Docker container is running. 
* `-u`: By default, the PostgreSQL image uses a username **postgres** that you can use to log in to the database.

You can now run SQL queries against this database! 

### ✏️ Exercise 1: Connect to the PostgreSQL instance using pgAdmin
Now that you know how to connect using the CLI, try to do the same with the pgAdmin client. 

### ✏️ Exercise 2: Create a database
Create a new database called `<First Name initial><Last Name>`, i.e. Harry Potter `hpotter`.

### Stop your services! 
Don't forget to stop your containers when you are done.