"""
2017 Tom Cuypers
"""
from typing import List, Dict, Any  # pylint: disable=W0611

class Playlist(object):
    """
    Represents a playlist
    """
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.music_files = list()  # type: List[Dict[str, Any]]
        self.playlist_type = ""  # type: str
        self.load()

    def save(self) -> None:
        """
        Save playlist to file
        """
        black_list = ['url', 'length', 'name']
        with open(self.filename, 'w') as fileptr:
            fileptr.write('#' + self.playlist_type + '\n')
            for music_file in self.music_files:
                for key, value in (music_file).items():
                    if key not in black_list:
                        fileptr.write('#' + key + ':' + value)
                fileptr.write('#EXTINF:%(length)d,%(name)s\n' % music_file)
                fileptr.write(music_file.get('url') + '\n')

    def load(self) -> None:
        """
        load playlist from file
        """
        with open(self.filename, 'r') as fileptr:
            index = 0  # type: int
            music_file = dict()  # type: Dict[str, Any]
            for line in fileptr:  # type: str
                line = line.replace('\n', '')
                if line != "":
                    if index == 0:
                        self.playlist_type = line[1:]
                    elif line.lower().startswith('#extinf:'):
                        [key, value] = line[1:].split(':')
                        [length, name] = value.split(',')
                        music_file['name'] = name
                        music_file['length'] = int(length)
                    elif line.startswith('#'):
                        [key, value] = line[1:].split(':')
                        music_file[key] = value
                    else:
                        music_file['url'] = line
                        self.music_files += [music_file]
                        music_file = dict()
                    index += 1

