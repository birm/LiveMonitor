from distutils.core import setup

files=["Monitors/*"]

setup(name='LiveMonitor',
    version="1.2.3",
    description="Live async checks on the status of your network services and devices. Check port status, see networked host information, and check log summaries. API and application. Working on testing, API engine, and sample user interface.",
    author="Ryan Birmingham",
    author_email="birm@rbirm.us",
    url="http://rbirm.us",
    packages=['LiveMonitor'],
    package_data={'LiveMonitor':files},
    long_description=open('README').read(),
    install_requires=["netaddr"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Topic :: System :: Monitoring",
    ],
)
