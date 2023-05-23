import os.path

from django.http import HttpResponse

from ml.settings import BASE_DIR, MEDIA_ROOT


def send_file(file_name):
    # file = open('../tweet_data/' + str(file_name) + '.json')
    # file = open(os.path.join(MEDIA_ROOT, str(file_name) + '.json'))
    # print(os.path.join(os.path.dirname(os.path.dirname(__file__)), '/'))
    print(BASE_DIR)
    print(os.path.join(MEDIA_ROOT, str(file_name) + '.json'))
    # return HttpResponse(file, content_type='text/csv')

    response = HttpResponse(open(os.path.join(MEDIA_ROOT, str(file_name) + '.json'), encoding="utf-8").read())
    response['Content-Type'] = 'text/csv'
    response['Content-Disposition'] = 'attachment; filename=' + str(file_name) + '.csv'
    return HttpResponse(response, content_type='text/json')


def main():
    return


if __name__ == "__main__":
    main()
