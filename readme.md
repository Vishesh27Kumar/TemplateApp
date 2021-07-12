
## Steps for setting up this repository

```bash
1. python3 -m venv env
2. source env/bin/activate
3. pip install -r prerequisites/requirement.txt
4. sudo systemctl start mongod
```

## Setup auth database

```bash
$ mongo
```
```bash
> use engine-users
> db.createUser(
  {
    user: "engine-master",
    pwd: passwordPrompt(),  // or cleartext password
    roles: [{ role: "readWrite", db: "te" }]
  }
)
```

## Migrate system templates 
```bash
$ MONGODB_MIGRATIONS_CONFIG=migrations/test_config.ini mongodb-migrate
```

## Run server
```bash
$ python manage.py runserver
```