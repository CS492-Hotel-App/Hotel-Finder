# main file where we can run our app from
# server will run on 'localhost:5000' by default

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

