import os


def get_files_path_by_suffix(rootpath, suffix):
    res = []
    for (dirpath, dirnames, filenames) in os.walk(rootpath):
        for filename in filenames:
            if filename.startswith('.'):
                continue
            if filename.lower().endswith(suffix.lower()):
                res.append(dirpath + '/' + filename)
    return res


if __name__ == '__main__':
    rootpath = os.getcwd() + '/_posts'
    catalog = ['# catalog']
    for index, pyfile in enumerate(get_files_path_by_suffix(rootpath, '.md')):
        print('found', pyfile)
        filename = pyfile[pyfile.rfind('/') + 1:]
        catalog.append(f'+ [{filename}](_posts/{filename})')
    with open('README.md', 'w') as f:
        f.write('\n'.join(catalog))
