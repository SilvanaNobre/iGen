import support.app_object as app_object

app = app_object.app

@app.route('/')
@app.route('/')
def index():
    return render_template('index.html',
                           ufs=map_support.getUFs(),
                           municipios=map_support.getMunicipios('AC'))


if __name__ == '__main__':
    app.run()
