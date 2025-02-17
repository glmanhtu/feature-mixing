import os.path

from .regex import ImageFolder


class WriterZoo:

    @staticmethod
    def new(desc, **kwargs):
        return ImageFolder(desc['path'], regex=desc['regex'], **kwargs)

    @staticmethod
    def get(dataset, set, base_dir, **kwargs):
        _all = WriterZoo.datasets
        d = _all[dataset]
        s = d['set'][set]

        s['path'] = os.path.join(base_dir, s['path'])
        return WriterZoo.new(s, **kwargs)

    datasets = {

        'hisfrag20': {
            'basepath': '/data/mpeer',
            'set': {
                'test' :  {'path': 'test',
                                  'regex' : {'writer': '(\d+)', 'page': '\d+_(\d+)', 'fragment' : '\d+_\d+_(\d+)'}},

                'train' :  {'path': 'train',
                                  'regex' : {'writer': '(\d+)', 'page': '\d+_(\d+)', 'fragment' : '\d+_\d+_(\d+)'}},
            }
        },

        'papyrow' : {
            'basepath': '/data/mpeer',
            'set': {
                'complete': {'path': '/data/mpeer/papyri_1200/croppedImages',
                            'regex' : {'writer': '(^[^_]+)', 'page': '((?<=_)[^_]+(?=_))', 'fragment' : '((?<=_)[^_]*(?=\.[^.]+$))'}}
            }
        },
        'papyrow_binarized' : {
            'basepath': '/data/mpeer',
            'set': {
                'complete': {'path': '/data/mpeer/papyri_1200/binarized_sauvola',
                            'regex' : {'writer': '(^[^_]+)', 'page': '((?<=_)[^_]+(?=_))', 'fragment' : '((?<=_)[^_]*(?=\.[^.]+$))'}}
            }
        },
        'papyrow_unet_binarized' : {
            'basepath': '/data/mpeer',
            'set': {
                'complete': {'path': '/data/mpeer/papyri_1200/binarized_unet_2',
                            'regex' : {'writer': '(^[^_]+)', 'page': '((?<=_)[^_]+(?=_))', 'fragment' : '((?<=_)[^_]*(?=\.[^.]+$))'}}
            }
        }
    }
    


