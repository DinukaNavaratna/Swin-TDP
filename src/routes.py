from .principle import generateImages, dashboard, feedback, y_academic

def initialize_routes(api):
    api.add_resource(generateImages, "/generateImages")
    api.add_resource(dashboard, "/dashboard")
    api.add_resource(feedback, "/feedback")
    api.add_resource(y_academic, "/y_academic_attendance")