# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['Name']

# %% ../nbs/00_core.ipynb 3
class Name:
    """This class greets user """
    def __init__(self,a):
        self.a = a
    def name(self):
        """This function greets the user with name."""
        return f"greetings !!!! {self.a}"
    
