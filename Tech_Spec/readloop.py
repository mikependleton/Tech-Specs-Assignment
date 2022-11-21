def read_file(request):

    f = open("media/convert_2019_to_standard.txt")
    for line in f:
        print(line)  # Or do whatever you wish to line

    f.close()
