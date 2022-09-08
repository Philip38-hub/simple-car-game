started = False
while True:
    command = input('> ').lower()
    if command == 'help':
        print('''
Start- to start the car
stop- to stop the car
quit- to exit''')
    elif command == 'start':
        if started:
            print('car is already started!')
        else:
            started = True
            print('car started... ready to go')
    elif command == 'stop':
        if not started:
            print('car is stopped!')
        else:
            started = False
            print('car stopped')
    elif command == 'quit':
        break
    else:
        print('command unknown')
