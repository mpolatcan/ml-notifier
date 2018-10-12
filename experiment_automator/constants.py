import time


class ExperimentConstants:
    KEY_EXPERIMENT = "experiment"
    KEY_EXPERIMENT_NAME = "name"
    KEY_EXPERIMENT_PARAMS = "params"
    KEY_EXPERIMENT_PARAM_RANGE = "range"
    KEY_EXPERIMENT_WORKDIR = "workdir"


class SlackConstants:
    # TODO Edit default Slack notifications
    DEFAULT_NOTIFICATIONS = {
        "success": {
            "pretext": "Info from Experiment Automator",
            "title": "Model Training Success!",
            "text": "",
            "thumb_url": "",
            "color": "#7CD197",
            "footer": "Experiment Automator",
            "time": time.time()
        },
        "fail": {
            "pretext": "Info from Experiment Automator",
            "title": "Model Training Failed!",
            "text": "",
            "thumb_url": "",
            "color": "#F35A00",
            "footer": "Experiment Automator",
            "time": time.time()
        }
    }
    KEY_SLACK = "slack"
    KEY_SLACK_NOTIFICATION_FORMAT = "notification_format"
    KEY_SLACK_WEBHOOK_URL = "webhook_url"
    KEY_SLACK_NOTIFICATION_SUCCESS = "success"
    KEY_SLACK_NOTIFICATION_FAIL = "fail"
    KEY_SLACK_NOTIFICATION_PRETEXT = "pretext"
    KEY_SLACK_NOTIFICATION_TITLE = "title"
    KEY_SLACK_NOTIFICATION_THUMB_URL = "thumb_url"
    KEY_SLACK_NOTIFICATION_IMAGE = "image"
    KEY_SLACK_NOTIFICATION_COLOR = "color"
    KEY_SLACK_NOTIFICATION_FOOTER = "footer"
    KEY_SLACK_NOTIFICATION_TS = "ts"
    KEY_SLACK_ATTACHMENTS = "attachments"
    KEY_SLACK_FIELDS = "fields"
    KEY_SLACK_FIELD_TITLE = "title"
    KEY_SLACK_FIELD_VALUE = "value"
    KEY_SLACK_FIELD_SHORT = "short"
    KEY_SLACK_IMAGE_SERVICE = "image_service"
    KEY_SLACK_IMAGE_SERVICE_UPLOAD_URL = "upload_url"
    VALUE_SLACK_NOTIFICATION_FORMAT = "default"


class CSVReporterConstants:
    KEY_CSV = "csv"
    KEY_CSV_FILENAME = "filename"
    KEY_CSV_FORMAT = "csv_format"
    KEY_CSV_FORMAT_SEPARATOR = "separator"
    KEY_CSV_FORMAT_COLUMNS = "columns"
    KEY_CSV_STATUS = "status"
    VALUE_CSV_ENABLED = "enabled"
    VALUE_CSV_DISABLED = "disabled"


class OAuthConstants:
    KEY_OAUTH = "oauth"
    KEY_OAUTH_SERVICE_NAME = "service_name"
    KEY_OAUTH_CLIENT_KEY = "client_key"
    KEY_OAUTH_CLIENT_SECRET = "client_secret"
    KEY_OAUTH_REQUEST_TOKEN_URL = "request_token_url"
    KEY_OAUTH_ACCESS_TOKEN_URL = "access_token_url"
    KEY_OAUTH_AUTHORIZATION_URL = "authorization_url"
    KEY_OAUTH_BASE_URL = "base_url"
    KEY_OAUTH_CALLBACK = "oauth_callback"
    KEY_OAUTH_VERIFIER = "oauth_verifier"
    KEY_OAUTH_TOKEN = "oauth_token"
    KEY_OAUTH_TOKEN_SECRET = "oauth_token_secret"
    KEY_OAUTH_ACCESS_TOKEN_PATH = "access_token_path"
    KEY_OAUTH_CALLBACK_OOB = "oob"


class DriveConstants:
    KEY_DRIVE = "drive"


class FlickrConstants:
    FLICKR_OAUTH_REQUEST_TOKEN_URL = "https://www.flickr.com/services/oauth/request_token"
    FLICKR_OAUTH_AUTHORIZATION_URL = "https://www.flickr.com/services/oauth/authorize"
    FLICKR_OAUTH_ACCESS_TOKEN_URL = "https://www.flickr.com/services/oauth/access_token"
    FLICKR_OAUTH_BASE_URL = "https://api.flickr.com/services/rest"
    FLICKR_UPLOAD_URL = "https://up.flickr.com/services/upload/"
    FLICKR_GET_IMAGE_SIZES_METHOD = "flickr.photos.getSizes"
    FLICKR_IMAGE_TYPE_SQUARE = "Square"
    FLICKR_IMAGE_TYPE_LARGE_SQUARE = "Large Square"
    FLICKR_IMAGE_TYPE_THUMBNAIL = "Thumbnail"
    FLICKR_IMAGE_TYPE_SMALL = "Small"
    FLICKR_IMAGE_TYPE_ORIGINAL = "Original"


class OtherConstants:
    KEY_DEBUG = "debug"
    KEY_DEBUG_TRACEBACK = "debug_traceback"
    KEY_EXEC_STATUS = "exec_status"
    KEY_ERROR_CAUSE = "error_cause"
    EXECUTION_STATUS_SUCCESS = "SUCCESS"
    EXECUTION_STATUS_FAILED = "FAILED"
    IMAGE_SERVICE_FLICKR = "flickr"
