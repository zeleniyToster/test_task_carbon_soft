"""Скрипт Setup.py для проекта по упаковке."""
import copy

from setuptools import setup, find_packages

import os


def read_dependencies():
    """Получаем из requirements.txt зависимости по умолчанию."""
    filepath = os.path.join(os.path.dirname(__file__), 'server', 'cpu_checker', 'requirements.txt')
    with open(filepath) as requirements_file:
        dependencies = requirements_file.readlines()
        return [dependency for dependency in dependencies]


def extend_find_packages() -> list[str]:
    server_pkg = find_packages(where='server')
    client_pkg = find_packages(where='client')
    return server_pkg + client_pkg


if __name__ == '__main__':
    setup(
        name='test_task_carbon_soft',
        version='0.1.1',
        author='Basov Ivan',
        author_email='demon_cuc@mail.ru',
        url='https://github.com/zeleniyToster/test_task_carbon_soft',
        download_url='https://github.com/zeleniyToster/test_task_carbon_soft/archive/refs/heads/master.zip',
        package_dir={'': 'server',
                     'clientpkg': 'client'},
        packages=['server', 'client'],
        description='Тестовое задание для carbon soft.',
        python_requires='>=3.10.4',
        install_requires=[
              *read_dependencies(),
        ],
    )
