from flask import Flask, request
import hyphen

hyphen.importing.EXPECTED_EMPTY += [
    'Database',
    'Database.Sql',
    'Database.Sql.Util',
    'Database.Sql.Vertica',
    'Demo',
    'Text',
    'Text.PrettyPrint.HughesPJ.Doc'
]

import hs.Demo
import hs.Data.Text.Lazy
import hs.Text.PrettyPrint.HughesPJ

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/query', methods=['POST'])
def query():
    query = request.form['query']
    query_hs = hs.Data.Text.Lazy.fromChunks([query])
    result = hs.Demo.demoAllAnalyses(query_hs)
    return hs.Text.PrettyPrint.HughesPJ.render(result)

if __name__ == '__main__':
    app.run()
