class TipoY(object):

    def __init__(self):
        self.accion = 'creando'
        print('Tipo Y. Accion: {0}'.format(self.accion))
        return

    def hacer(self):
        self.accion = 'haciendo'
        print('Tipo Y. Accion: {0}'.format(self.accion))
        return

class TipoX(object):

    def __init__(self):
        self.accion = 'creando'
        self.t = TipoY()
        print('Tipo X. Accion: {0}'.format(self.accion))
        return

    def resolver(self):
        self.t.hacer()
        self.accion = 'haciendo algo'
        print('Tipo V. Accion: {0}'.format(self.accion))
        return

if __name__ == '__main__':
    x = TipoX()
    x.resolver()