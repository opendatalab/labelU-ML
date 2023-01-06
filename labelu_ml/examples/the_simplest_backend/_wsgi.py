from labelu_ml.api import init_app
from .model import MyModel

my_model = MyModel()

app = init_app(my_model)

def init_kwargs(**kwargs):
    my_model.__init__(**kwargs)


