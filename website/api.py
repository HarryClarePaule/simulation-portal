from flask_restful import Api, Resource, reqparse, abort
from . import models
from . import db


# data to be parsed from POST request from HPC's
database_args = reqparse.RequestParser()
database_args.add_argument("availability", type=str, required=True)
database_args.add_argument("user_online", type=str, required=True)
database_args.add_argument("comsol_online", type=str, required=True)
database_args.add_argument("time", type=str, required=True)

#  This class handles the API POST request
class HPCdata(Resource):
    def post(self, hpc_id):
        args = database_args.parse_args()
        update_table = models.HPCTable.query.filter_by(HPC_id=hpc_id).first()  # fetch HPC object
        if not update_table:
            abort(404, message="Could not find HPC with that id")
        update_table.Availability = args['availability']
        update_table.User_online = args['user_online']
        db.session.commit()

        return 'POST request successful', 201

# ---------- Old Code ---------- #
#  This class handles the API POST request
# class HPCdata(Resource):
#     def post(self, hpc_id):
#         args = database_args.parse_args()
#         result = models.HPCTable.query.filter_by(HPC_id=hpc_id).first()
#         if not result:
#             abort(404, message="Could not find HPC with that id")
#         update_table = models.HPCTable.query.filter_by(HPC_id=hpc_id).first()  # fetch HPC object
#         update_table.Availability = args['availability']
#         update_table.User_online = args['user_online']
#         db.session.commit()

#         return 'POST request successful', 201