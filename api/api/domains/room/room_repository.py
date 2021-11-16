from abc import ABC, abstractmethod
from typing import List, Optional

class TodoRepository(ABC):

    @abstractmethod
    def create():
      pass

    @abstractmethod
    def find_by_id():
      pass

    @abstractmethod
    def update():
      pass

    @abstractmethod
    def delete_by_id():
      pass
