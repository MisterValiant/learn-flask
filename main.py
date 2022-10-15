from website import create_app

app=create_app()

# Only if we run this file, we are going to run the next line
if __name__ == '__main__':
    app.run(debug=True)