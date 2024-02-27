import threading

thread_object = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs = {'sep' : ' & '})

# args = arguments, kwargs = keyword arguments

thread_object.start()