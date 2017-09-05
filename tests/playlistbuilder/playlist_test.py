"""
Tom Cuypers 2017
"""

from playlistbuilder import playlist
import unittest
import os
import contextlib
import filecmp

class PlaylistTest(unittest.TestCase):

    def test_load_save(self) -> None:
        play_list = playlist.Playlist(filename="data/PLAYLIST.m3u8")
        self.assertEqual(len(play_list.music_files), 1)
        self.assertEqual(play_list.music_files[0].get('name'), 'Lovin\' Me')
        self.assertEqual(play_list.music_files[0].get('length'), 277)
        self.assertEqual(play_list.music_files[0].get('url'), '04 Lovin Me.mp3')
        play_list.filename = 'temp.txt'
        with contextlib.suppress(FileNotFoundError):
            os.remove('temp.txt')
        play_list.save()
        filecompare = filecmp.cmp('temp.txt', 'data/PLAYLIST.m3u8', shallow=False)
        self.assertTrue(filecompare)
