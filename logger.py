import datetime
import json
import pprint

def get_args_kwargs(*args, **kwargs):
    dict_args = {'args': args[1:]}
    dict_kwargs = {'kwargs': kwargs}
    list_param = [dict_args, dict_kwargs]
    return list_param

def path_logs(path):
    def decor_logger(old_function):
        def new_function(*args, **kwargs):
            start = str(datetime.datetime.now())
            result = {
                'time': start,
                'function_name': old_function.__name__,
                'arguments': get_args_kwargs(*args, **kwargs),
                'result': old_function(*args, **kwargs)
            }
            try:
                with open(path, encoding='utf-8') as f:
                    res_list = json.load(f)
            except Exception:
                res_list = []
            else:
                with open(path, encoding='utf-8') as f:
                    res_list = json.load(f)
            res_list.append(result)
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(res_list, f, ensure_ascii=False, indent=2)
            return res_list
        return new_function
    return decor_logger