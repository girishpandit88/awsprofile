awsprofile
======================

This small little python package allows you to quickly switch between different iam profile by making them default one.

#####Installation
Installing from source:
```
git clone git@github.com:girishpandit88/awsprofile.git
cd awsprofile
python setup.py install
```
Installing via pip:
```pip install awsprofile```

#####Usage
```awsprofile <profile_to_be_used_as_default>```

then you can run any ```aws``` command without the ```--profile <profilename>``` passed as argument to ```aws``` command

Once you are done you can switch back to using default aws profile by running ```awsprofile```

#####In near future
Ability to give custom path to the credential file.
