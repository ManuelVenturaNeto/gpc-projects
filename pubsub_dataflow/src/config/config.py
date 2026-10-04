import os


class Settings():

    def __init__(self):
        self.PROJECT_ID = os.getenv('PROJECT_ID', 'pets-482115')
        self.REGION = os.getenv('REGION', 'us-central1')
        self.BUCKET = os.getenv('BUCKET', 'teste-dataflow')
        self.TOPIC_NAME = os.getenv('TOPIC_NAME', 'exemplo')
        self.SUBSCRIPTION = os.getenv('SUBSCRIPTION', 'sub-exemplo')

    def credential(self):
        os.environ.setdefault(
            'GOOGLE_APPLICATION_CREDENTIALS',
            '/app/teste-sa.json' if os.path.exists('/app/teste-sa.json') else 'teste-sa.json'
        )


settings = Settings()
settings.credential()