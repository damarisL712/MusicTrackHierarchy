Author name: Damaris Lubin 


# Music Track Hierarchy

## Project Overview

This project is a Python object-oriented programming assignment that models different types of media tracks using inheritance and polymorphism.

The program includes a shared abstract base class called `MusicTrack` and two concrete subclasses:

- `Song`
- `Podcast`

Supporting classes are also used to represent artists, albums, and playlists.

The project demonstrates how common data and behavior can be placed in a parent class and reused by multiple subclasses.

---

## Project Goals

The main goals of this project are to practice:

- Object-oriented programming in Python
- Inheritance
- Polymorphism
- Abstract base classes
- Abstract methods
- `@property` getters
- Encapsulation
- Defensive copying
- Default parameters
- Method overriding
- Comparison dunder methods
- Sorting custom objects
- Pytest unit testing
- Incremental Git commits

---

## Class Hierarchy

```text id="hyy15f"
MusicTrack
├── Song
└── Podcast
```

Supporting classes:

```text id="afcv1l"
Artist
Album
Playlist
```

`MusicTrack` contains the fields and methods that are shared by both `Song` and `Podcast`.

`Song` and `Podcast` inherit from `MusicTrack` and provide their own implementation of `play_time_formatted()`.

---

## Project Structure

```text id="pebwun"
F26_IST242_ASG06_music_<yourname>/
│
├── artist.py
├── album.py
├── music_track.py
├── song.py
├── podcast.py
├── playlist.py
├── main.py
├── test_music.py
├── requirements.txt
└── README.md
```

### `artist.py`

Contains the `Artist` class.

The class stores:

- Artist or creator name
- Genre

The values are stored using non-public attributes and exposed through read-only properties.

---

### `album.py`

Contains the `Album` class.

The class stores:

- Album or show title
- Whether it is currently active
- A list of years in which content was released

The class also:

- Raises a `ValueError` if the years list is empty
- Uses defensive copying to protect the internal years list
- Provides a derived `debut_year` property

---

### `music_track.py`

Contains the abstract `MusicTrack` base class.

This class stores the fields shared by both songs and podcasts:

- Artist
- Album
- Duration in seconds

It also provides:

- A derived `release_year` property
- An abstract `play_time_formatted()` method
- A concrete `total_play_time()` method
- Comparison methods used to compare tracks by release year

Because `MusicTrack` is abstract, it cannot be instantiated directly.

---

### `song.py`

Contains the `Song` class.

`Song` inherits from `MusicTrack`.

Songs display their duration using the format:

```text id="ihoj8c"
MM:SS
```

Example:

```text id="ytoqcq"
220 seconds → 03:40
```

---

### `podcast.py`

Contains the `Podcast` class.

`Podcast` inherits from `MusicTrack` and adds:

- `is_explicit`

The `is_explicit` value defaults to `False`.

Podcasts display their duration using the format:

```text id="op3jsr"
HH:MM:SS
```

Example:

```text id="ap9iv8"
9000 seconds → 02:30:00
```

---

### `playlist.py`

Contains the `Playlist` class.

A playlist stores multiple `MusicTrack` objects.

It supports:

- Adding tracks
- Clearing the playlist
- Sorting tracks by release year
- Returning a protected copy of the track list
- Displaying each track on a separate line

Because both `Song` and `Podcast` inherit from `MusicTrack`, the playlist can contain both types at the same time.

---

### `main.py`

The main program demonstrates the complete class hierarchy.

It creates:

- Two songs
- Two podcasts
- One playlist

The tracks are displayed first in their original insertion order and then sorted by release year.

---

### `test_music.py`

Contains the instructor-provided Pytest test suite.

The tests check:

- Artist properties
- Album validation and defensive copying
- Abstract class behavior
- Song formatting
- Podcast formatting
- Track comparisons
- Playlist behavior
- Sorting
- Integration between all classes

---

## Example Program Behavior

Before sorting, tracks appear in the order they were added to the playlist.

After sorting, tracks are ordered by their release year.

Example:

```text id="1s9zet"
Before sorting:
(Kendrick Lamar, Hip-Hop) DAMN. active = True, debut year: 2017, duration: 03:40
(Alanis Morissette, Alternative) Jagged Little Pill active = False, debut year: 1995, duration: 04:05
(Joe Rogan, Comedy) The Joe Rogan Experience active = True, debut year: 2009, duration: 02:30:00 is explicit: True
(Sarah Koenig, Journalism) Serial active = False, debut year: 2014, duration: 01:30:00 is explicit: False
```

After sorting:

```text id="ha2556"
(Alanis Morissette, Alternative) Jagged Little Pill active = False, debut year: 1995, duration: 04:05
(Joe Rogan, Comedy) The Joe Rogan Experience active = True, debut year: 2009, duration: 02:30:00 is explicit: True
(Sarah Koenig, Journalism) Serial active = False, debut year: 2014, duration: 01:30:00 is explicit: False
(Kendrick Lamar, Hip-Hop) DAMN. active = True, debut year: 2017, duration: 03:40
```


