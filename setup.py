from distutils.core import setup

files=["Monitors/*"]

setup(name='LiveMonitor',
    version="0.1",
    description="Live async checks on the status of your network services and devices. Check port status, see networked host information, and check log summaries. API and application.",
    author="Ryan Birmingham",
    url="http://rbirm.us",
    packages=['LiveMonitor'],
    package_data={'LiveMonitor':files},
    long_description=open('README').read(),
    install_requires=["json","paramiko"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Topic :: System :: Monitoring",
    ],
)
