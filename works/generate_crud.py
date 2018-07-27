'''
1, finish the model
2, change the init func
3, run the script to generate crud code
'''
import os
import json
root_path = os.getcwd()


class Model:

    def __init__(self, Model, fields):
        self.Model = Model
        self.model = Model.lower()  # TODO 驼峰转下划线
        self.create_field = json.dumps(list(
                fields ^ self.create_exclude_fields))
        self.update_field = json.dumps(list(
                fields ^ self.update_exclude_fields))

    @property
    def create_exclude_fields(self):
        return self.update_exclude_fields | {'status'}

    @property
    def update_exclude_fields(self):
        return {}


class Generate:
    templates = {'test': '''
def test_crud_{model}(stub):
    # test list
    res = stub.List{Models}({proto}_pb2.ListReq(ipp=10, page=1))
    assert res.total == 0
    # test create
    create_data = {create_data_assign}
    stub.Create{Model}({proto}_pb2.Create{Model}Req(**create_data))
    res = stub.List{Models}({proto}_pb2.ListReq(ipp=10, page=1))
    assert res.total == 1
    obj_id = res.objects[0].id
    for k, v in create_data.items():
        assert getattr(res.objects[0], k) == v
    # test update
    update_data = create_data.update({update_data_assign})
    update_data['id'] = obj_id
    stub.Update{Model}({proto}_pb2.Update{Model}Req(**update_data))
    res = stub.Get{Model}(base_pb2.IdReq(id=obj_id))
    for k, v in update_data.items():
        assert getattr(res, k) == v
    # test delete
    stub.Delete{Model}(base_pb2.IdReq(id=obj_id))
    res = stub.List{Models}({proto}_pb2.ListReq(ipp=10, page=1))
    assert res.total == 0

''', 'service': '''
    def Create{Model}(self, request, context):
        data = msg2dict(request, {create_field})
        return {Model}.create_by_dict(data).to_message({proto}_pb2.{Model})

    def Get{Model}(self, request, context):
        obj = {Model}.get_by_id(request.id)
        return obj.to_message({proto}_pb2.{Model})

    def List{Models}(self, request, context):
        page, ipp = request.page, filter_ipp(request.ipp)
        objs, total = {Model}.list_by_page(ipp, page)
        return {proto}_pb2.{Models}(
                objects=objs, page=page, ipp=ipp, total=total)

    def Delete{Model}(self, request, context):
        {Model}.delete_{model}(request.id)
        return base_pb2.DefaultRes()

    def Update{Model}(self, request, context):
        data = msg2dict(request, {update_field})
        return {Model}.update_by_dict(data).to_message({proto}_pb2.{Model})

''', 'model': '''


''', 'proto': '''


'''}

    def __init__(self, model_file, service_file, test_file,
                 proto_file):
        self.file_paths = {
                'test': test_file, 'service': service_file,
                'model': model_file, 'proto': proto_file}
        self.model = None

    @property
    def model(self):
        return self.model

    @model.setter
    def model(self, obj):
        self.model = obj

    @property
    def param(self):
        if self.model_helper is None:
            return {}
        # TODO use payload generate self.param
        payload = [
            'model', 'Models', 'Model', 'create_data_assign', 'proto',
            'update_data_assign', 'create_field', 'update_field']

    def write_to_file(self):
        for file_type, template in self.templates:
            with open(self.file_paths[file_type], 'a') as f:
                f.write(template.format(**self.param))


model_helper = ModelHelper('Theme', {
    'title', 'zip_name', 'zip_index', 'status'})
generate = Generate(
        model_helper,
        os.path.join(root_path, 'app/models.py'),
        os.path.join(root_path, 'app/services.py'),
        os.path.join(root_path, 'tests/models.py'),
        os.path.join(root_path, '../protos/readingfoundation/service.proto'))
generate.write_to_file()
