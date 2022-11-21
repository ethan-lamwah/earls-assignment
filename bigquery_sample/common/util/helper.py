import os


def setup_google_adc(use_default = False):
    # Set up authentication via Application Default Credentials (ADC)
    if use_default or os.environ.get('GOOGLE_APPLICATION_CREDENTIALS') is None:
        # use demo credentials
        google_app_credentials = os.path.abspath('credentials/bigquerysample-demo.json')
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = google_app_credentials
