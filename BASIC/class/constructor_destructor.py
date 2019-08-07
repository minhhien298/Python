# Tham khảo https://www.geeksforgeeks.org/destructors-in-python/


class Employee:
    # Initializing
    def __init__(self):
        print('Employee created.')

    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')


obj = Employee()
del obj
