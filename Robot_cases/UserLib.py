class UserLib():
    def __init__(self):
        self.first_title = 'XPL(1)/200 SAP Easy Access'

    def is_first(self, title):
        if title == self.first_title:
            print(f'The title of window is {title}')
        else:
            raise AssertionError(f'The title of window shoul be {self.first_title} but is {title}')