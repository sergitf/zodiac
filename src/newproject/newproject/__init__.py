from pyramid.config import Configurator
from resources import Root
import views
import pyramid_jinja2
import os

__here__ = os.path.dirname(os.path.abspath(__file__))


def make_app():
    """ This function returns a Pyramid WSGI application.
    """
    settings = {}
    settings['mako.directories'] = os.path.join(__here__, 'templates')
    config = Configurator( root_factory=Root, settings=settings )
    config.add_renderer('.jinja2', pyramid_jinja2.Jinja2Renderer)
    config.add_view(views.zodiac_view,
                    context=Root,
                    renderer='zodiac.mako')
    config.add_static_view(name='static',
                           path=os.path.join(__here__, 'static'))
    
    config.add_route( "home", "/home" )
    config.add_view( views.home_view, route_name="home", renderer="home.mako" )
    
    
    config.add_route( "zodiac", "/zodiac" )
    config.add_view( views.zodiac_view, route_name="zodiac", renderer="zodiac.mako" )
    
    config.add_route( "consulta", "/consulta" )
    config.add_view( views.consulta_view, route_name="consulta", renderer="consulta.mako" )
    
    return config.make_wsgi_app()

application = make_app()
