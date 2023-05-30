from . import db


class MaterialsDatabase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isotropic = db.Column(db.Boolean)
    classification = db.Column(db.String(500)) 
    Material_name = db.Column(db.String(500), unique=True)
    density = db.Column(db.Float)
    elastic_modulus_x = db.Column(db.Float)
    elastic_modulus_y = db.Column(db.Float)
    elastic_modulus_z = db.Column(db.Float)
    poissons_ratio_x = db.Column(db.Float)
    poissons_ratio_y = db.Column(db.Float)
    poissons_ratio_z = db.Column(db.Float)
    tensile_yield_x = db.Column(db.Float)
    tensile_yield_y = db.Column(db.Float)
    tensile_yield_z = db.Column(db.Float)
    tensile_ultimate_x = db.Column(db.Float)
    tensile_ultimate_y = db.Column(db.Float)
    tensile_ultimate_z = db.Column(db.Float)
    brinell_hardness = db.Column(db.Float)
    rockwell_hardness = db.Column(db.Float)
    vickers_hardness = db.Column(db.Float)
    material_damping_ratio = db.Column(db.Float)
    coef_therm_exp_x = db.Column(db.Float)
    coef_therm_exp_y = db.Column(db.Float)
    coef_therm_exp_z = db.Column(db.Float)
    therm_conduct_x = db.Column(db.Float)
    therm_conduct_y = db.Column(db.Float)
    therm_conduct_z = db.Column(db.Float)
    spec_heat_cap = db.Column(db.Float)
    temp_limit_op_max = db.Column(db.Float)
    temp_limit_op_min = db.Column(db.Float)
    temp_limit_non_op_max = db.Column(db.Float)
    temp_limit_non_op_min = db.Column(db.Float)



class HPCTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    HPC_id = db.Column(db.String(4096), unique=True)
    HPC_specs = db.Column(db.String(4096))
    COMSOL_licences = db.Column(db.String(4096))
    Additional_licences = db.Column(db.String(4096))
    Availability = db.Column(db.String(4096))
    User_online = db.Column(db.String(4096))


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    HPC_id = db.Column(db.String(4096))
    comment = db.Column(db.String(10000))
