import wikipedia


def wikipedia_command(command):
    cmd, keyword = command.split(maxsplit=1)
    wikipedia.set_lang('ja')
    try:
        page = wikipedia.page(keyword)
        title = page.title
        page_sum = page.summary
        response = 'タイトル:{}\n{}'.format(title, page_sum)
    except wikipedia.exceptions.PageError:
        response = '{}のページが見つかりませんでした'.format(keyword)
    return response

