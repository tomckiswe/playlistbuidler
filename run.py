"""
2017 Tom Cuypers
"""

import argparse
import logging
import glob
from os.path import expanduser
from typing import Dict, List, Any  # pylint: disable=W0611
import tornado.web  # type: ignore
from playlistbuilder import playlist

class Playlistbuilder(object):
    """
    The main server code
    """
    def __init__(self, config: Dict[str, Any]) -> None:   # pylint: disable=E1136
        self.port = config.get('port', 5432)  # type: int
        self.playlists = list()  # type: List[playlist.Playlist]
        self.music_directory = expanduser(config.get('music_location', '~/music'))  # type: str
        self.webinterface = tornado.web.Application(handlers=[
            (r"/admin/(.*)", tornado.web.StaticFileHandler, {"path": "webinterface", "default_filename": "index.html"}),
        ])  # type: tornado.web.Application
        self.webinterface.listen(port=self.port)
        self.load_playlists()

    def run(self) -> None:
        """
        Run tornado and cron server
        """
        tornado.ioloop.IOLoop.current().start()

    def load_playlists(self) -> None:
        """
        Check for all playlists in the music directory and load them
        """
        for playlist_filename in glob.glob(self.music_directory + "/*.m3u8"):
            self.playlists += [playlist.Playlist(filename=playlist_filename)]

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
    playlist_config = vars(args)
    playlistbuilder = Playlistbuilder(config=playlist_config)
    playlistbuilder.run()
