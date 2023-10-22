from .principle import dashboard, feedback, academic, k6, manbox, masculinity, engagement, growthmindset
from .teacher import Tdashboard, Tfeedback, Tk6, Tdisrespect, Tmanbox, Tmasculinity, Tengagement, Tgrowthmindset, Tstudent

def initialize_routes(api):
    api.add_resource(dashboard, "/dashboard")
    api.add_resource(feedback, "/feedback")
    api.add_resource(academic, "/academic/<type>")
    api.add_resource(k6, "/k6/<type>")
    api.add_resource(manbox, "/manbox/<type>")
    api.add_resource(masculinity, "/masculinity/<type>")
    api.add_resource(engagement, "/engagement/<type>")
    api.add_resource(growthmindset, "/growthmindset/<type>")
    api.add_resource(Tdashboard, "/Tdashboard")
    api.add_resource(Tfeedback, "/Tfeedback")
    api.add_resource(Tk6, "/Tk6")
    api.add_resource(Tdisrespect, "/Tdisrespect")
    api.add_resource(Tmanbox, "/Tmanbox")
    api.add_resource(Tmasculinity, "/Tmasculinity")
    api.add_resource(Tengagement, "/Tengagement")
    api.add_resource(Tgrowthmindset, "/Tgrowthmindset")
    api.add_resource(Tstudent, "/Tstudent")