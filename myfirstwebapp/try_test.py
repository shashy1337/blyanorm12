import sys
try:
    with open('file.txt', 'a') as fh:
        file = fh.read()
        print(file)

except FileNotFoundError:
    print('Data is missing')

except PermissionError:
    print('This is not allowed')

except Exception as err:
    print('Some other error occured:', str(err))

try:
    1/0
except:
    err = sys.exc_info()
    for e in err:
        print(e)

