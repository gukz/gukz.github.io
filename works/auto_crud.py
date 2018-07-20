import inspect

def get_models():
    from app import models
    from peewee import Model
    modules = [import_module('.'.join([modules.__name__, modname])) for
               _, modname, _ in pkgutil.iter_modules(models.__path__)]
    return [model for module in modules for _, model in inspect.getmembers(
            module, lambda x: inspect.isclass(x) and issubclass(x, Model))]



def get_model_fields(model):
    return []


def create_api(model):
    pass


def get_field_data(fields):
    res = {}
    for field in fields:
        if field in ['id', 'status', 'updated_at', 'created_at']:
            continue
        res[field] = 'field'


def create_test(module, model):
    template = '''
    def test_crud_{model_name}(stub):
        res = stub.List{ModelNames}({module}_pb2.List{ModelNames}Req(
            ipp = 10, page = 1))
        assert res.total == 0
        data =
        res = stub.Create{ModelName}({module}_pb2.Create{ModelName}Req(
            **data))
        assert res.id == 1

    '''
