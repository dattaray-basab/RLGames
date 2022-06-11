import os
from shutil import rmtree


def cleanup_mgr():
    _files_to_remove = ['.DS_Store']
    _directories_to_remove = ['__pycache__', '.pytest_cache', '__DATA']
    _directories_to_avoid = ['Archives', 'venv']
    def fn_clean(dirpath):
        for item in os.listdir( dirpath ):
            child_path = os.path.join( dirpath, item )
            if os.path.isdir( child_path ):
                if item not in _directories_to_avoid:
                    if item in _directories_to_remove:
                        rmtree( child_path )
                    else:
                        fn_clean( child_path )
                else:
                    print('Skipped: {}'.format(child_path))
            else:
                if item in _files_to_remove:
                    os.remove(child_path)
                    x = 1
        # end for
    return fn_clean

if __name__ == '__main__':
    root_dirpath = os.path.abspath( '..' )
    fn_clean = cleanup_mgr()
    fn_clean(root_dirpath)

