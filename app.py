import os
from config import app, db
from posts.index import posts

app.register_blueprint(posts, url_prefix='/posts')


@app.before_first_request
def cria_banco():
    db.create_all()


if __name__ == '__main__':
    app.run(host = app.config['HOST'], port = app.config['PORT'], debug = app.config['DEBUG'])
