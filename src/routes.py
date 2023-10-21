from .principle import analysis, dashboard

def initialize_routes(api):
    api.add_resource(analysis, "/analysis")
    api.add_resource(dashboard, "/dashboard")