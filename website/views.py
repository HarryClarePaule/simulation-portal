from flask import Blueprint, render_template, request, flash, jsonify, redirect, abort
from .models import HPCTable, Note
from . import db
import json

views = Blueprint('views', __name__)

def get_notes_by_id():
    hpc_ids = ['NA_DT_07', 'NA_DT_04', 'NA_DT_01', 'NA_DT_09', 'NA_DT_10', 'NA_DT_02', 'NA_DT_03', 'NA_DT_19', 'NA_DT_08', 'NA_DT_20', 'NA_DT_21', 'NA_LT_122']
    return {hpc_id: Note.query.filter_by(HPC_id=hpc_id).all() for hpc_id in hpc_ids}

@views.route('/')
def home():
    return render_template("home.html")


@views.route('/HPCtable', methods=['GET', 'POST'])
def hpc_table():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is empty', category='error')
        else:
            HPC_id = request.form.get('HPC_id')
            print(HPC_id)
            new_note = Note(comment=note, HPC_id=HPC_id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added', category='success')

    return render_template("index.html",
                HPC_database=HPCTable.query.all(),
                notes=Note.query.all(),
                **get_notes_by_id()
                )
#---------- Old Code ----------#
    # return render_template("index.html",
    #                        HPC_database=HPCTable.query.all(),
    #                        notes=Note.query.all(),
    #                        NA_DT_07=Note.query.filter_by(HPC_id='NA_DT_07').all(),
    #                        NA_DT_04=Note.query.filter_by(HPC_id='NA_DT_04').all(),
    #                        NA_LT_122=Note.query.filter_by(HPC_id='NA_LT_122').all(),
    #                        NA_DT_01=Note.query.filter_by(HPC_id='NA_DT_01').all(),
    #                        NA_DT_09=Note.query.filter_by(HPC_id='NA_DT_09').all(),
    #                        NA_DT_10=Note.query.filter_by(HPC_id='NA_DT_10').all(),
    #                        NA_DT_02=Note.query.filter_by(HPC_id='NA_DT_02').all(),
    #                        NA_DT_03=Note.query.filter_by(HPC_id='NA_DT_03').all(),
    #                        NA_DT_19=Note.query.filter_by(HPC_id='NA_DT_19').all(),
    #                        NA_DT_08=Note.query.filter_by(HPC_id='NA_DT_08').all(),
    #                        NA_DT_20=Note.query.filter_by(HPC_id='NA_DT_20').all(),
    #                        NA_DT_21=Note.query.filter_by(HPC_id='NA_DT_21').all(),
    #                        )


@views.route('/api/table-update')
def table_update():
    return render_template("hpcTable.html", 
                            HPC_database=HPCTable.query.all(),
                            notes=Note.query.all(),
                            **get_notes_by_id()
                          )



@views.route('/matDB')
def material_database():
    
    return render_template("matDB.html",
                        HPC_database=HPCTable.query.all(),
                        notes=Note.query.all(),
                        **get_notes_by_id()
                        )
#---------- Old Code ---------- #
    # return render_template("matDB.html",
    #                         HPC_database=HPCTable.query.all(),
    #                         notes=Note.query.all(),
    #                         NA_DT_07=Note.query.filter_by(HPC_id='NA_DT_07').all(),
    #                         NA_DT_04=Note.query.filter_by(HPC_id='NA_DT_04').all(),
    #                         NA_LT_122=Note.query.filter_by(HPC_id='NA_LT_122').all(),
    #                         NA_DT_01=Note.query.filter_by(HPC_id='NA_DT_01').all(),
    #                         NA_DT_09=Note.query.filter_by(HPC_id='NA_DT_09').all(),
    #                         NA_DT_10=Note.query.filter_by(HPC_id='NA_DT_10').all(),
    #                         NA_DT_02=Note.query.filter_by(HPC_id='NA_DT_02').all(),
    #                         NA_DT_03=Note.query.filter_by(HPC_id='NA_DT_03').all(),
    #                         NA_DT_19=Note.query.filter_by(HPC_id='NA_DT_19').all(),
    #                         NA_DT_08=Note.query.filter_by(HPC_id='NA_DT_08').all(),
    #                         NA_DT_20=Note.query.filter_by(HPC_id='NA_DT_20').all(),
    #                         NA_DT_21=Note.query.filter_by(HPC_id='NA_DT_21').all(),
    #                        )


#---------- Old Code ----------#
# @views.route('/delete-note', methods=['POST'])
# def delete_note():
#     note = json.loads(request.data)
#     noteId = note['id']
#     note = Note.query.get(noteId)
#     db.session.delete(note)
#     db.session.commit()

#     return jsonify({})

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['id']
    note = Note.query.get(noteId)
    if note:
        db.session.delete(note)
        db.session.commit()
    else:
        abort(404, message="Could not find note with that id")

    return jsonify({})




@views.route("/calculators")
def calculators():
    return render_template("calculators.html")


@views.route("/add_data")
def add_data():
    # with open('website/database.json') as f:
    #     data = json.load(f)
    # for i in data:
    #     check = HPCTable.query.filter_by(HPC_id=i["hpc_id"]).first()
    #     print(check)
    #     if not check:
    #         new_pc = HPCTable(
    #             HPC_id=i["hpc_id"],
    #             HPC_specs=i["lic_specs"],
    #             COMSOL_licences=i["comsol_lic"],
    #             Additional_licences=i["add_lic"],
    #             Availability=i["availability"],
    #             User_online=i["user_online"]
    #         )
    #         print(f'computer {new_pc.HPC_id} added')
    #         db.session.add(new_pc)
    #         db.session.commit()

    # delete = HPCTable.query.filter_by(HPC_id='NA-DT-07').first()
    # db.session.delete(delete)
    # db.session.commit()

    # update = HPCTable.query.filter_by(HPC_id='NA-DT-02').first()
    # update.HPC_specs='CPU 16 cores 2.8GHz | 256 GB RAM | Nvidia Quadro P2200'
    # update.COMSOL_licences='Licence: NSL Saulius Rackauskas [10072818] \n1. MECHANICAL 2. THERMAL 3. CAD IMPORT 4. SW LIVELINK 5. RF'
    # db.session.commit()
    return render_template("home.html", database=MaterialsDatabase.query.all())

