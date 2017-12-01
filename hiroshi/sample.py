import tasks


def top_page_task(top_page_url):

    print('<first task>')
    # ここでタスク起動　(runタスク)
    worker = tasks.get_top_page_links.delay(top_page_url)
    while not worker.ready():
        pass
    print (worker.result)

    worker = tasks.get_child_page_links.delay()
    while not worker.ready():
        pass
    print (worker.result)


if __name__ == '__main__':
    # ---------------------- Category(parent)  items & URLs ----------------------------------------
    '''
    メルカリのTOP の　category　parent を取得
    '''
    top_page_url='https://www.mercari.com/jp/'
    child_page_url="https://www.mercari.com/jp/category/1/"
    top_page_task(top_page_url)
    # print(category)


