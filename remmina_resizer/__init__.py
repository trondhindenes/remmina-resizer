import os
from screeninfo import get_monitors
from ruamel.yaml import YAML


def main():
    home = os.getenv('HOME')
    settings_file = os.path.join(home, '.remmina-resizer.yml')
    if os.path.exists(settings_file):
        print('found settings file {}'.format(settings_file))
        settings = load_settings(settings_file)
    else:
        print('did not find settings file ({}), using default'.format(settings_file))
        settings = {
            'default': {
                'reduce_width': 40,
                'reduce_height': 111
            },
            '1920x1080': {
                'reduce_width': 40,
                'reduce_height': 111
            }
        }
    xdg_data_home = os.getenv('XDG_DATA_HOME', os.path.join(home, '.local/share/remmina'))
    print('Looking for remmina connection files at at {}'.format(xdg_data_home))
    height, width = get_optimal_screen_resolution(settings)
    print('Optimal resolution: height: {}, width: {}'.format(str(height), str(width)))

    remmina_files = os.listdir(xdg_data_home)
    for conn_file in remmina_files:
        conn_file_full_path = os.path.join(xdg_data_home, conn_file)
        adjust_remmina_resolution(conn_file_full_path, height, width)

def load_settings(settings_file):
    print('loading settings file {}'.format(settings_file))

    with open(settings_file, 'r') as stream:
        settings_file_contents = stream.read()

    yaml = YAML(typ='safe')
    settings = yaml.load(settings_file_contents)
    return settings

def adjust_remmina_resolution(conn_file, height, width):
    with open(conn_file, 'r') as stream:
        file_contents = stream.readlines()

    is_rdp_file = False
    for line in file_contents:
        if line.startswith('protocol'):
            if line == 'protocol=RDP' + os.linesep:
                is_rdp_file = True
    newlines = []
    for line in file_contents:
        if line.startswith('resolution_height'):
            line = 'resolution_height={}'.format(str(height)) + os.linesep
        elif line.startswith('resolution_width'):
            line = 'resolution_width={}'.format(str(width)) + os.linesep
        elif line.startswith('resolution='):
            line = 'resolution={}x{}'.format(str(width), str(height)) + os.linesep
        newlines.append(line)
    print('adjusting file {}'.format(conn_file))
    with open(conn_file, 'w') as stream:
        stream.writelines(newlines)


def get_optimal_screen_resolution(settings):
    screen_size = get_monitors()[0]
    height, width = screen_size.height, screen_size.width
    settings_item = '{}x{}'.format(width, height)
    print('current resolutoin is {}'.format(settings_item))
    if settings_item in settings:
        print('using setting for resolution {}'.format(settings_item))
    else:
        print('loading default settings')
        settings_item = 'default'
    reduce_height = settings[settings_item]['reduce_height']
    reduce_width = settings[settings_item]['reduce_width']

    height = height-reduce_height
    width = width-reduce_width
    return height, width


if __name__ == '__main__':
    main()
