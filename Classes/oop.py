import django

class Transportation:
    def __init__(self,mode,sub) -> None:
        self.mode=mode
        self.sub=sub

UnitedStates=Transportation('air','us air lines')
print(UnitedStates.mode)
print(django.get_version())