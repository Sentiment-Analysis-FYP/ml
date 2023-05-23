from django.http import HttpResponse


def send_file(file_name):
    file = open('../tweet_data/' + str(file_name))
    return HttpResponse(file, content_type='text/csv')


def main():
    return


if __name__ == "__main__":
    main()
