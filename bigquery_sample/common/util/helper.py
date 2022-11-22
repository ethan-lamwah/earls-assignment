from django.conf import settings
import os


def setup_google_adc():
    default_user_credentials = settings.USE_GCLOUD_APPLICATION_DEFAULT_CREDENTIALS
    
    if default_user_credentials or os.environ.get('GOOGLE_APPLICATION_CREDENTIALS') is None:
        # use default user credentials
        google_app_credentials = os.path.abspath('credentials/application_default_credentials.json')
        # print(f'The following credential is used: {google_app_credentials}')
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = google_app_credentials
        # Set GCLOUD_PROJECT to fix 'Project was not passed and could not be determined from the environment.'
        os.environ["GCLOUD_PROJECT"] = "bigquerysample-369121"
