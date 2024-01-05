class LockedClass:
    __slots__ = ('first_name',)

    def __setattr__(self, name, value):
        if not hasattr(self, 'first_name') and name != 'first_name':
            raise AttributeError(f"Cannot create new instance attribute '{name}'. Only 'first_name' is allowed.")
        super().__setattr__(name, value)


locked_obj = LockedClass()
locked_obj.first_name = "John"
print(locked_obj.first_name)
