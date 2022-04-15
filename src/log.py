import os, sys, logging, bugsnag
from bugsnag.handlers import BugsnagHandler


class Log():

    def __init__(self):

        self.logger = logging.getLogger("scum")

        # stream handler
        stream_handler = logging.StreamHandler(sys.stdout)
        self.logger.addHandler(stream_handler)

        working_dir = os.getcwd()
        bugsnag.configure(
            api_key="8b60d1890a58f9fcc3dc8627809a361a",
            project_root=working_dir,
            release_stage=os.environ.get("BUGSNAG_STAGE", "production")
        )
        handler = BugsnagHandler()
        # send only ERROR-level logs and above
        handler.setLevel(logging.ERROR)
        self.logger.addHandler(handler)
