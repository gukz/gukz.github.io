import os
from datetime import datetime, date


def generate_note_title(mdfile):
    title = mdfile[mdfile.rfind('/') + 12:mdfile.rfind('.')]
    with open(mdfile, 'r') as f:
        lines = [line.strip('# ') for line in f.read().split('\n')
                 if line.strip('# ') != '']
        if lines:
            title = lines[0]
    return title


def get_files_path_by_suffix(rootpath, suffix):
    res = []
    for (dirpath, dirnames, filenames) in os.walk(rootpath):
        for filename in filenames:
            if filename.startswith('.'):
                continue
            if filename.lower().endswith(suffix.lower()):
                res.append(dirpath + '/' + filename)
    return res


def get_md_files_name():
    rootpath = os.getcwd() + '/_posts'
    catalog = []
    for index, pyfile in enumerate(get_files_path_by_suffix(
                rootpath, '.md')):
        filename = pyfile[pyfile.rfind('/') + 1:]
        try:
            datetime.strptime(filename[:10], '%Y-%m-%d')
        except ValueError:
            filename = '{}-{}'.format(
                    date.today(), filename)
            new_pyfile = pyfile[:pyfile.rfind('/')+1] + filename
            os.rename(pyfile, new_pyfile)
            print('rename', filename)
            pyfile = new_pyfile
        catalog.append('[{}](_posts/{})'.format(
                generate_note_title(pyfile), filename))
    return catalog


def update_readme():
    catalog = ['# catalog'] + get_md_files_name()
    with open('README.md', 'w') as f:
        f.write('\n'.join(catalog))


if __name__ == '__main__':
    update_readme()
