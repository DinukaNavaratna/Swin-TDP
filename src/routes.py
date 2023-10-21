from .principle import generateImages, dashboard, feedback

def initialize_routes(api):
    api.add_resource(generateImages, "/generateImages")
    api.add_resource(dashboard, "/dashboard")
    api.add_resource(feedback, "/feedback")