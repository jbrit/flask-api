import os
app_config = {
    'SQLALCHEMY_DATABASE_URI': os.environ.get("DATABASE_URL").replace("postgres://", "postgresql://"),
    'DEBUG': True,
}