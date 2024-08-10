import os
import logging

from browserstack.local import Local
from browserstack_sdk import BrowserStackSdk

logger = logging.getLogger('app_logger')


def run_tests_on_browserstack(context):
    context.browserstack_local = BrowserStackSdk(bs_local_args)
    context.browserstack_local.start()

    bs_local_args = {
        "key": "nzs6xqzRkUfyod4F9Grd",
        "localIdentifier": "elakkiaduraisamy_6lZMFK",
        "forcelocal": "true",
        "onlyAutomate": "true",
        "logFile": "./logs/browserstack_local.log"
    }

    bs_config = {
        "os": context.app_platform_config["platform_name"],
        "os_version": context.app_platform_config["platform_version"],
        "device": context.app_platform_config["device_name"],
        "real_mobile": "true",
        "project": "My Mobile Automation Project",
        "build": "Dev Build",
        "name": context.scenario.name,
        "app": context.app_platform_config["app_path"],
        "browserstack.local": "true",
        "browserstack.localIdentifier": "elakkiaduraisamy_6lZMFK"
    }
    # Start BrowserStack Local
    context.browserstack_local = Local()
    context.browserstack_local.start(**bs_local_args)

    logger.info("Running tests on BrowserStack")

    # Example: Change 'tests/features/login.feature' to the specific file you want to run
    os.system(f'behave tests/features/login.feature -D platform={context.input_platform_name} --tags=-@skip')

    # Stop BrowserStack Local
    context.browserstack_local.stop()
    logger.info("Finished running tests on BrowserStack")
