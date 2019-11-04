from api.grpc.grpc_server import GrpcServer
from engine import Engine

import time

import alembic.config
alembicArgs = [
    '--raiseerr',
    'downgrade', '-1',
]
alembic.config.main(argv=alembicArgs)

alembicArgs = [
    '--raiseerr',
    'upgrade', 'head',
]
alembic.config.main(argv=alembicArgs)

engine = Engine()

''' GRPC api '''
grpc = GrpcServer(engine)
grpc.start_server()
print('GRPC server started...')
    
''' Loop as nothing is blocking '''
try:
    while True:
        time.sleep(60*60*60)
except KeyboardInterrupt:
    grpc.stop_server()
