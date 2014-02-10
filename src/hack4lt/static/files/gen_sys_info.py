import sys
from hashlib import md5
from subprocess import Popen, PIPE


version_commands = [
    ('lsb_release -a', 4),
    ('python -V', 1),
    ('vim --version', 1),
    ('git --version', 1),
    ('hg --version', 1)
]
config_files = ['~/.vimrc', '~/.gitconfig', '~/.hgrc']
sys_info = ''

for command, number_of_rows in version_commands:
    resp = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = resp.communicate()
    stdout = stdout.decode("utf-8")
    stderr = stderr.decode("utf-8")
    info = stderr.strip()
    if stdout:
        info = '\n'.join(stdout.split('\n')[:number_of_rows])
    sys_info += info + '\n\n'

for config_file in config_files:
    cmd = 'cat {0}'.format(config_file)
    response = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    file_hash = md5(response.communicate()[0]).hexdigest()
    sys_info += '{0} MD5 checksum: {1}\n'.format(config_file, file_hash)

output_filename = 'sys_info'
if len(sys.argv) > 1:
    output_filename = sys.argv[1]

with open(output_filename, 'w') as output_file:
    output_file.write(sys_info)
    print('System info was dumped into "{0}" file\n'.format(output_filename))
    print('System info: \n{0}'.format(sys_info))
