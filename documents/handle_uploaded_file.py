def handle_uploaded_file(f, name):
    destination = open('/Users/Oliver/Documents/macademia/media/'+name, 'w+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()