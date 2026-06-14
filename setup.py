from setuptools import setup, find_packages

setup(
    name='youtube_comment_analyzer',
    version='1.0.0',
    author='Siddhartha Ganguli',
    author_email='siddharthaganguli0093@gmail.com',
    description='A tool to analyze YouTube comments using NLP techniques.',
    licence='MIT',
    package_dir={'' : 'src'},
    packages=find_packages(where='src'),
    include_package_data=True
        


)