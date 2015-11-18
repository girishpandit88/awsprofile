#!/usr/bin/python
import os, sys, ConfigParser

import sys
sys.tracebacklimit = 0
aws_access_key_id = 'aws_access_key_id'
aws_secret_access_key = 'aws_secret_access_key'
config = ConfigParser.RawConfigParser()

# config.read(['credential', os.path.expanduser('~/.aws/credentials')])
def opt_move(configuration, section1, section2, option):
	try:
		configuration.set(section2, option, configuration.get(section1, option))
	except ConfigParser.NoSectionError:
		# Create non-existent section
		configuration.add_section(section2)
		opt_move(configuration, section1, section2, option)


def use_profile(profile_name):
	config.read(os.path.expanduser('~/.aws/credentials'))
	try:
		config.get(profile_name,aws_access_key_id)
	except ConfigParser.NoSectionError:
		if profile_name=='':
			pass
		else:
			raise Exception('No such config')
	if profile_name == '' or profile_name == 'default':
		print('no profile name, trying to switch back to default profile...')
		if config.has_section('tmp'):
			opt_move(config, 'tmp', 'default', aws_access_key_id)
			opt_move(config, 'tmp', 'default', aws_secret_access_key)
			config.remove_section('tmp')
			with open(os.path.expanduser('~/.aws/credentials'), 'wb') as configfile:
				config.write(configfile)
				print('switched to default profile')
				sys.exit()

	elif profile_name is not None and profile_name not in 'default':
		if config.has_section('tmp'):
			print('Credential file was already swapped once, please run aws_profile once without any argument to continue')
			sys.exit()
		print('Switching default profile to ', profile_name)
		def_access_key = config.get('default', aws_access_key_id)
		def_secret_key = config.get('default', aws_secret_access_key)
		opt_move(config, profile_name, 'default', aws_access_key_id)
		opt_move(config, profile_name, 'default', aws_secret_access_key)
		config.add_section('tmp')
		config.set('tmp', aws_access_key_id, def_access_key)
		config.set('tmp', aws_secret_access_key, def_secret_key)
		with open(os.path.expanduser('~/.aws/credentials'), 'wb') as configfile:
			config.write(configfile)


def main():
	if len(sys.argv) < 2:
		use_profile('')
	else:
		use_profile(sys.argv[1])


if __name__ == "__main__":
	main()



