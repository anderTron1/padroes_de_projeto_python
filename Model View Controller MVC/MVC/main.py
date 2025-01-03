from tornado import ioloop, httpserver
from tornado.web import Application

from controllers.produto_controller import Index, Novo, Atualiza, Deleta
from pathlib import Path

class RunApp(Application):
    def __init__(self):
        handlers = [
            (r'/', Index),
            (r'/produto/novo', Novo),
            (r'/produto/update/(\d+)/status/(\d+)', Atualiza),
            (r'/produto/delete/(\d+)', Deleta)
        ]
        base_path = Path(__file__).parent

        settings = dict(
            debug = True,
            template_path= base_path / 'views',  # Corrigido o nome
            static_path= base_path / 'static',  # Caminho absoluto recomendado
            xsrf_cookies=False
        )

        Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    http_server = httpserver.HTTPServer(RunApp())
    http_server.listen(5000)
    ioloop.IOLoop.instance().start()