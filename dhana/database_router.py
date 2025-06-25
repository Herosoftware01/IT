class MasterRouter:
    models = {'*'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'dhana':
            if model._meta.model_name in self.models:
                return 'demo'
            return 'mssql'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'dhana':
            if model._meta.model_name in self.models:
                return 'demo'
            return 'mssql'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'dhana':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'dhana':
            if model_name in self.models:
                return db == 'demo'
            return db == 'mssql'
        return db == 'default'
