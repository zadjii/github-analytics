from app import app

# for local development:
#   this path will let us run the app for local testing with `python wsgi.py`
# For deployment:
#   We're setting the entrypoint module for uwsgi as `module = wsgi:app`, which
#   will use the `app` that we import above.
if __name__ == "__main__":
    app.run()
