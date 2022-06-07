from invoke import task


@task
def run(c):
    # c.run("python3 ./manage.py makemigrations")
    # c.run("python3 ./manage.py migrate")
    c.run("python3 ./manage.py runserver 0.0.0.0:8000")
