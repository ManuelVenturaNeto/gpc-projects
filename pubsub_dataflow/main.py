import logging
from src.pubsub import generate_data
from src.storage import create_bucket
from src.dataflow import create_dataflow

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(name)s %(levelname)s, %(message)s",
        #filename="./pipeline_logs.log",
    )

    create_bucket()
    generate_data()
    create_dataflow()