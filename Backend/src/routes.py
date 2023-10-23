from .principle import dashboard, feedback, academic, k6, manbox, masculinity, engagement, growthmindset, clubs
from .outsider import Odashboard, Ofeedback, Oacademic, Ok6, Omanbox, Omasculinity, Oengagement, Ogrowthmindset, Oclubs
from .teacher import Tdashboard, Tfeedback, Tk6, Tdisrespect, Tmanbox, Tmasculinity, Tengagement, Tgrowthmindset, Tstudent, Tdata, Tadjanency
from .student import Sdashboard, Snominations, Scolleague

def initialize_routes(api):
    api.add_resource(dashboard, "/dashboard")
    api.add_resource(feedback, "/feedback")
    api.add_resource(academic, "/academic/<type>")
    api.add_resource(k6, "/k6/<type>")
    api.add_resource(manbox, "/manbox/<type>")
    api.add_resource(masculinity, "/masculinity/<type>")
    api.add_resource(engagement, "/engagement/<type>")
    api.add_resource(growthmindset, "/growthmindset/<type>")
    api.add_resource(clubs, "/clubs")
    
    api.add_resource(Tdashboard, "/Tdashboard")
    api.add_resource(Tfeedback, "/Tfeedback")
    api.add_resource(Tk6, "/Tk6")
    api.add_resource(Tdisrespect, "/Tdisrespect")
    api.add_resource(Tmanbox, "/Tmanbox")
    api.add_resource(Tmasculinity, "/Tmasculinity")
    api.add_resource(Tengagement, "/Tengagement")
    api.add_resource(Tgrowthmindset, "/Tgrowthmindset")
    api.add_resource(Tstudent, "/Tstudent")
    api.add_resource(Tdata, "/Tdata")
    api.add_resource(Tadjanency, "/Tadjanency")
    
    api.add_resource(Sdashboard, "/Sdashboard")
    api.add_resource(Snominations, "/Snominations")
    api.add_resource(Scolleague, "/Scolleague")
    
    api.add_resource(Odashboard, "/Odashboard")
    api.add_resource(Ofeedback, "/Ofeedback")
    api.add_resource(Oacademic, "/Oacademic/<type>")
    api.add_resource(Ok6, "/Ok6/<type>")
    api.add_resource(Omanbox, "/Omanbox/<type>")
    api.add_resource(Omasculinity, "/Omasculinity/<type>")
    api.add_resource(Oengagement, "/Oengagement/<type>")
    api.add_resource(Ogrowthmindset, "/Ogrowthmindset/<type>")
    api.add_resource(Oclubs, "/Oclubs")