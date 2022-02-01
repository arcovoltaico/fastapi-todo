PyCharm New project with new environment

from terminal:
source venv/bin/activate

maybe PyCharm won't have the same interpreter on its terminal, 
so we would need to restart it.

then:

`pip install sqlalchemy`
`pip install psycopg2-binary` (the Postgress driver)
`pip install alembic`

`pip freeze > requirements.txt`

`alembic init alembic`

Sync the DB with initial user records
`python src/database/run_seeder.py devuser`

TODO:
- Convert model/db  into a TODO app (task, type, deadline, done)
- populate type ('home','work', 'admin','education', 'hobby')
- create scripts to list, add, update name, done, delete task
- install FastAPI to allow those CRUD operations be done from url endpoints
