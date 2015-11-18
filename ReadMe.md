awsprofile
======================

This small little python package allows you to quickly switch between different iam profile by making them default one.

#####Installation
Installing from source:
```
git checkout git@github.com:girishpandit88/awsprofile.git
cd awsprofile
python setup.py install
```
Installing via pip:
```pip install awsprofile```

#####Usage
Assuming your credentials are stored in ```~/.aws/credentials``` folder.
```awsprofile <profile_to_be_used_as_default>```

then you can run any aws command with ```--profile <profilename>``` 

Once you are done you can switch back to using default aws profile by running ```awsprofile```

Please Note this package allows you to switch between default and any other iam profile. Once you switch between default and iam profile, you have to run awsprofile with no arguments before you can switch with any other profile. 

#####In near future
Ability to give custom path to the credential file.
