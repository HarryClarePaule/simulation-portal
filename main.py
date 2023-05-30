from flask_restful import Api
from website import create_app
import website.api

app = create_app()

# -------------------- This section is for API code -------------------- #
api = Api(app)
HPCdata = website.api.HPCdata

# sets up API endpoint
api.add_resource(HPCdata, "/<string:hpc_id>")  # requires HPC id in POST request to work

# ---------------------------------------------------------------------- #

if __name__ == '__main__':
    app.run(debug=True)



