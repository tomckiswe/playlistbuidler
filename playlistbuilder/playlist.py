"""
2017 Tom Cuypers
"""
from typing import List

class Playlist(object):

    def __init__(self, filename: str) -> None:
        self.music_files = []  # type: List[str]

    def save(self):
        pass

    def load(self):
        pass