from fabric.api import run
from fabric.api import env, cd

env.hosts = ['161.35.97.158']
env.user = 'emi'
env.key_filename='/Users/emisaar/.ssh/id_rsa.pub'

def deploy():
    print('Deploying...')
    with cd('django-bootcamp'):
        with cd('CodigoFacilito-Django-Bootcamp'):
            run('git pull')
            run('ls')
