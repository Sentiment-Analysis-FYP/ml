from django.http import HttpResponse


def send_file(file_name):
    file = open('../tweet_data/' + str(file_name))
    # return HttpResponse(file, content_type='text/csv')

    response = HttpResponse(open("../tweet_data/" + str(file_name), 'rb').read())
    response['Content-Type'] = 'text/csv'
    response['Content-Disposition'] = 'attachment; filename=' + str(file_name) + '.csv'
    return response


def main():
    return


if __name__ == "__main__":
    main()
