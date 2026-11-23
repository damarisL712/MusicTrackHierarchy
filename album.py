"""
Represents a music album or podcast series, including the years it was active.

Key concepts to implement:
  • Input validation in __init__ (fail-fast with a clear ValueError).
  • Defensive copy on both input and output so external code cannot corrupt
    the internal years list.
  • A *derived* property (debut_year) that computes its value from stored data
    rather than keeping a second field in sync.
"""
class Album: 
  def __init__(self, title, active, years):
    # make sure the years list is not empty
    if len(years) == 0:
      raise ValueError("years list cannot be empty")

    # store the album title
    self._title = title
    
    # store whether the album or show is active
    self._active = active 

    # store a copy of the years list
    self._years = years.copy()
  
  @property
  def title(self):
    # Return the album or show title
    return self._title
  
  @property
  def active(self):
    # return whether the album or show is active
    return self._active
  
  @property
  def years(self):
    # return a copy of years list so
    # outside code can't change the inter list directly
    return self._years.copy()
  
  @property
  def debut_year(self):
    # return the first year in the years list
    return self._years[0]

  def __str__(Self):
    # return a readable representation of the album or show
    return f"{self._title} active = {self._active}, debut year: {self.debut_year}"
