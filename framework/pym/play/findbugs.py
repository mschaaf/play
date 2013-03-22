import os, os.path, shutil

def findBugsConfig(dotSettings,app):
	findBugPrefs = os.path.join(dotSettings, 'edu.umd.cs.findbugs.core.prefs')

	if app.readConf('findbugs.config'):
		configuredFindBugs = app.readConf('findbugs.config')
		try:
			shutil.copyfile(configuredFindBugs,findBugPrefs)
			print "~ Findbugs configured successfully."
		except IOError:
			print "~ Error while creating findbugs config file!"
			pass
			