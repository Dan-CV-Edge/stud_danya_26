from setuptools import find_packages, setup

package_name = 'stud_danya_26'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='danul',
    maintainer_email='danul@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'first_node = stud_danya_26.first:main',
            'number_mode = stud_danya_26.number:main',
            'num_lis = stud_danya_26.num_list:main',
        ],
    },
)
