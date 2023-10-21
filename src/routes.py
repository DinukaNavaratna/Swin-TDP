from .principle import dashboard, feedback, y_academic, y_k6, y_manbox, y_masculinity, y_engagement, y_growthmindset

def initialize_routes(api):
    api.add_resource(dashboard, "/dashboard")
    api.add_resource(feedback, "/feedback")
    api.add_resource(y_academic, "/y_academic")
    api.add_resource(y_k6, "/y_k6")
    api.add_resource(y_manbox, "/y_manbox")
    api.add_resource(y_masculinity, "/y_masculinity")
    api.add_resource(y_engagement, "/y_engagement")
    api.add_resource(y_growthmindset, "/y_growthmindset")