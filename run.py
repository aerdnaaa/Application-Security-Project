from flaskr import app
import datetime

if __name__ == "__main__":

    app.config.update(
    SECRET_KEY = "WeakSecretKey",
    SESSION_COOKIE_HTTPONLY = False,
    SESSION_COOKIE_SECURE = False,
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=365)
    )
    # this is the finalized codes

    app.run()
