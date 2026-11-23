"""
Represents a musical artist or podcast creator.

This is the simplest class in the hierarchy — no dependencies, no validation.
It introduces two core Python OOP conventions:
  1. The single leading-underscore (_name) signals a non-public attribute.
  2. @property exposes a clean public getter without allowing direct mutation.
"""

class Artist:
  
  # Initialize the artist with it's name and genre
  def __init__(self,name,genre):
    # Store the artist's name and genre as non-public attributes
    self._name = name
    self._genre = genre

  @property
  def name(self):
    # return the artist's name
    return self._name

  @property
  def genre(self):
    # Return the artist's genre
    return self._genre

  def __str__(self):
    # Return a readable representation of the artist
    return f"{self._name}, {self._genre}"

