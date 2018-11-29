import random
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run

REPO_URL = 'https://github.com/doubleo46/angular_django'


def deploy():
    """Django deploy commands."""
    site_folder = f"/home/anoop/fabric/{env.user}/sites/{env.host}"
    run(f'mkdir -p {site_folder}')
    with cd(site_folder):
        _get_latest_source()
        _update_virtualenv()


def _get_latest_source():
    if exists('.git'):
        run('git fetch')
    else:
        run(f'git clone {REPO_URL} .')
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run(f'git reset --hard {current_commit}')

def _update_virtualenv():
    # run('pip install -r requirements.txt')
    pass
