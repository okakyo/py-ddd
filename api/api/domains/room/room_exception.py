class RoomsDoesNotFound(Exception):
  message = "This room does not found."
  def __str__(self) -> str:
      return RoomsDoesNotFound.message
