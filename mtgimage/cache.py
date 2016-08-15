from django.http import HttpResponse
import os
import shutil
import wget


def get_path(language, multiverse_id):
    return 'cached/' + language + '/' + multiverse_id


def get_link(language, multiverse_id):
    return 'cached/links/' + language + '/' + multiverse_id


def download(language, multiverse_id):
    url = 'http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=' + multiverse_id + '&type=card'
    wget.download(url, out=get_path(language, multiverse_id))


def response(language, multiverse_id):
    with open(get_path(language, multiverse_id), "rb") as f:
        return HttpResponse(f.read(), content_type="image/jpeg")


def translate_response(language, multiverse_id):
    with open(get_link(language, multiverse_id), "rb") as f:
        return HttpResponse(f.read(), content_type="image/jpeg")


def get_by_language(language, multiverse_id):
    try:
        return response(language, multiverse_id)
    except IOError:
        download(language, multiverse_id)
        return response(language, multiverse_id)


def link(language, english_multiverse_id, multiverse_id):
    source = get_path(language, multiverse_id)
    target = get_link(language, english_multiverse_id)
    if os.name == 'posix':
        os.symlink(os.getcwd() + '/' + source, target)
    else:
        shutil.copyfile(source, target)


def get_and_link_by_language(request, english_multiverse_id, multiverse_id, language):
    try:
        return response(language, multiverse_id)
    except IOError:
        download(language, multiverse_id)
        if not os.path.exists(get_path('en', english_multiverse_id)):
            download('en', english_multiverse_id)
        link(language, english_multiverse_id, multiverse_id)
        return response(language, multiverse_id)


def get(request, english_multiverse_id):
    return get_by_language('en', english_multiverse_id)


def get_translated(request, language, english_multiverse_id):
    try:
        return translate_response(language, english_multiverse_id)
    except IOError:
        return response('en', english_multiverse_id)
