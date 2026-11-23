"""
A collection class that holds MusicTrack objects (Songs and Podcasts).

Design notes:
  • _tracks is kept private (single underscore) and exposed as a *copy*
    through the `tracks` property to protect encapsulation.
  • clear_playlist() uses list.clear() rather than rebinding to None or a new
    list, so the internal object reference stays valid.
  • sort_by_release_year() delegates to list.sort(), which in turn calls
    MusicTrack.__lt__ — the comparison logic defined in Part 3 pays off here.
  • __str__ uses a generator expression with str.join() for a concise
    multi-line string without building an intermediate list manually.
"""
class Playlist:
  def __init__(self):
    # create an empty list to store MusicTrack objects
    self._tracks = []

  @property
  def tracks(self):
    # return a copy so outside code can't change the internal list
    return self._tracks.copy()
  
  def add_track(self, track):
    # add a track to the playlist
    self._tracks.append(track)
  
  def clear_playlist(self):
    # remove every track from the playlist
    self._tracks.clear()
  
  def sort_by_release_year(self):
    # sort the tracks in place using MusicTrack comparison methods
    self._tracks.sort()
  
  def __str__(self):
    # Return each track on its own line.
    return "\n".join(str(track) for track in self._tracks)