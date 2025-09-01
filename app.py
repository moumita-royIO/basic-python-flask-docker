from flask import Flask
from helper import articles  # articles dictionary

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>Welcome to Articles Library</h1>
    <p>Browse through the links below to explore articles:</p>
    <ul>
        <li><a href="/articles/cloudsecurity">Cloud Security</a></li>
    </ul>
    '''

@app.route('/articles/<category>')
def article_list(category):
    article_items = articles.get(category, [])
    if not article_items:
        return "<h1>No articles found</h1>", 404

    html = f'<h1>List of {category.capitalize()} Articles</h1>'
    html += '<ul>'

    for i, article in enumerate(article_items):
        html += f'''
        <li><a href="/articles/{category}/{i}">{article['title']}</a> 
        by {article['author']}</li>
        '''
    html += '</ul>'
    return html

@app.route('/articles/<category>/<int:article_id>')
def article_details(category, article_id):
    article_items = articles.get(category, [])
    if 0 <= article_id < len(article_items):
        article = article_items[article_id]
        return f'''
        <h1>{article['title']}</h1>
        <strong>Author:</strong> {article['author']}<br><br>
        <p>{article['summary']}</p>
        <a href="{article['url']}" target="_blank">Read Full Article</a><br><br>
        <a href="/articles/{category}">Back to {category.capitalize()} list</a>
        '''
    else:
        return "<h1>Article not found</h1>", 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
