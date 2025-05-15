
class BrokenCarError(Exception):
    pass

def drive_car(fuel, flat_tire):
    if fuel <= 0:
        raise BrokenCarError('Out of fuel!')
    if flat_tire:
        raise BrokenCarError('Flat_tire!')
    print('Car is running! Vroom Vroom!')

try:
    drive_car(0, True)
except BrokenCarError as error:
    print(f'Error: {error}')

drive_car(10, False)