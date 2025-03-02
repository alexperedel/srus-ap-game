class DeletionFromEmptyList(Exception):
    def __init__(self, message="Cannot delete from an empty list!"):
        super().__init__(message)
