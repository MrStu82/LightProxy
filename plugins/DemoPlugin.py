import LightPlugin
import logging

logger = logging.getLogger("SWProxy")

class DemoPlugin(LightPlugin.LightPlugin):
    def process_request(self, req_json, resp_json):
        logger.info("Found Summoners War API request : %s" % req_json['command'])
