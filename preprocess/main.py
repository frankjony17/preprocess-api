import logging
import os

from preprocess import create_app
from preprocess.util.middleware_controller import setup_metrics

app = create_app()
setup_metrics(app)


def start():
    port = int(os.environ.get('PORT', 9000))
    logging.getLogger('preprocess.main').info(f'Starting in port {port}.')
    app.run(host='0.0.0.0', port=port, debug=os.environ.get('MODE') != 'prod',
            use_reloader=os.environ.get('MODE') != 'prod')


if __name__ == '__main__':
    start()
