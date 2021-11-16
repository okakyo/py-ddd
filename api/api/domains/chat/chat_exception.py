class ChatMessageNotFound(Exception):
  message = "This message does not found"

  def __str__(self) -> str:
      return ChatMessageNotFound.message

