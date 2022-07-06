import support.app_object as app_object
import support.backend_functions

app = app_object.app

@app.route('/')
def index():
    return render_template('index.html',
                           ufs=support.backend_functions.CreateGraphFig(),
                           municipios=map_support.getMunicipios('AC'))


if __name__ == '__main__':
    app.run()
