from google.cloud import dataflow_v1beta3 as df
from .config import settings

client = df.FlexTemplatesServiceClient()

def create_dataflow():
    request = df.LaunchFlexTemplateRequest(
        project_id = settings.PROJECT_ID,
        region = settings.REGION,
        launch_parameter = df.LaunchFlexTemplateParameter(
            job_name = 'pubsub-to-bigquery',

            container_spec_gcs_path=f"gs://{settings.BUCKET}/templates/pubsub_to_bq.json",

            parameters={
                "input_subscription": f"projects/{settings.PROJECT_ID}/subscriptions/{settings.SUBSCRIPTION}",
                "output_table": f"{settings.PROJECT_ID}:dataset.tabela",
            },

            environment=df.FlexTemplateRuntimeEnvironment(
                temp_location=f"gs://{settings.BUCKET}/temp",
                max_workers=3,
                enable_streaming_engine=True,
            ),
        )
    )

    response = client.launch_flex_template(request=request)
    return response.job
