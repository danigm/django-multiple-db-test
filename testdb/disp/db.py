class DispRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'disp':
            return 'disp'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'disp':
            return 'disp'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if (obj1._meta.app_label == 'disp' and
            obj2._meta.app_label == 'disp'):
           return True
        elif (obj1._meta.app_label != 'disp' and
              obj2._meta.app_label != 'disp'):
           return True
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        if db == 'disp':
            return app_label == 'disp'
        elif app_label == 'disp':
            return db == 'disp'

        return True
