from flask import jsonify, request
from app.forms.book import SearchForm

from helper import is_isbn_or_key
from yushu_book import YuShuBook


from . import web


# @web.route('/book/search/<q>/<page>')
@web.route('/book/search/')
def search():
    q = request.args['q']
    page = request.args['page']

    form =SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q)
        return jsonify(result)
    else:
        return jsonify({'msg':'参数校验失败'})
