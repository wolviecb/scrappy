"""script de scrapping no site da Pfile_cache para verificacao de status do passaporte"""
def scrapper(url, regex):
    """gets url from argv[1] and pattern from argv[2] and return results from webpage"""
    import requests
    from lxml import html

    page = requests.get(url)
    tree = html.fromstring(page.content)
    status = tree.xpath(regex)

    return status

def file_handler(name, action, status=0):
    """should be called with file_handler(filename, r|w, status=optional)
    if called with r status is unused and the function returns the content of filename
    if called with w status is required and the functions will with status to filename"""
    import pickle
    if action == 'r':
        file_cache = open(name, "rb")
        last = pickle.load(file_cache)
        file_cache.close()
        return last
    elif action == 'w':
        file_cache = open(name, "wb")
        pickle.dump(status[len(status)-1].__str__(), file_cache)
        file_cache.close()


def check(url, dest="0", passwd="0"):
    """checka o site da PF e compara o status a execução anterior
    se tiver alteração printa a alteração e atualiza o arquivo de histórico
    senão retorna 'No change'"""
    from mailer import email
    regex = '//td/text()'
    status = scrapper(url, regex)
    last = file_handler('last.txt', 'r')


    if status[len(status)-1] == last:
        print("No change")
        if dest != "0" or passwd != "0":
            email(status, "No Change", dest, passwd)
    else:
        for i in status:
            print(i)
        if dest != "0" or passwd != "0":
            email(status, "NEW STATUS", dest, passwd)

        file_handler("last.txt", "w", status)
