from django.apps import AppConfig


class CommonConfig(AppConfig):
    name = 'common'

    # def ready(self):
    #     from actstream import registry
    #     registry.register(self.get_model('common'))
