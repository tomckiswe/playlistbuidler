"""
2017 Tom Cuypers
"""

import argparse
import logging
import tornado.web  # type: ignore
from typing import Dict, Any

class Playlistbuilder(object):
    """
    The main server code
    """
    def __init__(self, config: Dict[str, Any]) -> None:
        self.port = config.get('port', 5432)  # type: int
        self.music_directory = config.get('music_location', '~/music')  # type: str
        self.webinterface = tornado.web.Application(handlers=[
            (r"/admin/(.*)", tornado.web.StaticFileHandler, {"path": "webinterface", "default_filename": "index.html"}),
        ])  # type: tornado.web.Application
        self.webinterface.listen(port=self.port)

    def run(self) -> None:
        tornado.ioloop.IOLoop.current().start()

def parse_input():
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser(description='Run the playlistbuilder server')
    parser.add_argument('--port', default='5432', help='Sets the ')
    parser.add_argument('--music_location', default='~/music')
    return parser.parse_args()

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(levelname)-7s [%(module)-15s] %(message)s',
                        datefmt='%m/%d/%Y %H:%M:%S', level=logging.INFO)
    args = parse_input()
    config = vars(args)
    playlistbuilder = Playlistbuilder(config=config)
    playlistbuilder.run()
