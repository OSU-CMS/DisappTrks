#!/usr/bin/env python

import copy
import os
import re
import sys
import itertools
import json
import subprocess
import time
import cPickle as pickle

from threading import Thread, Lock, Semaphore, active_count
from multiprocessing import cpu_count

from OSUT3Analysis.Configuration.ProgressIndicator import ProgressIndicator

if len(sys.argv) < 2:
	print 'Usage: python findDuplicateLumisInDataset.py dataset'
	sys.exit(2)

datasetName = sys.argv[1]

dataset0 = re.sub (r"^\/([^/]*)\/([^/]*)\/([^/]*)$", r"\1", datasetName)
dataset1 = re.sub (r"^\/([^/]*)\/([^/]*)\/([^/]*)$", r"\2", datasetName)
dataset2 = re.sub (r"^\/([^/]*)\/([^/]*)\/([^/]*)$", r"\3", datasetName)

datasetLabel = dataset0 + '_' + dataset1 + dataset2

threads = []
printLock = Lock()
semaphore = Semaphore(cpu_count() + 1)

progress = ProgressIndicator("")

datasetFileContents = {} # datasetFileContents[file] = [(run, lumi), (run, lumi), ...]

def getLumisInFile(fileName, i, nFiles):
	global printLock
	global semaphore
	global datasetFileContents
	global datasetLabel

	semaphore.acquire()

	baseName = fileName[54:].replace('/', '.')

	if not os.path.exists('eventContentJSONs_' + datasetLabel + '/' + baseName):
		ps = subprocess.Popen('dasgoclient --query="lumi file=' + fileName + ' instance=prod/phys03" -json  > eventContentJSONs_' + datasetLabel + '/' + baseName, 
							  shell = True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		output = ps.communicate()[0]

	f = open('eventContentJSONs_' + datasetLabel + '/' + baseName, 'r')
	data = json.load(f)
	f.close()

	# intermediateList = [(run1, [lumis in run1]), (run2, [lumis in run2]), ...]
	intermediateList = [(x['lumi'][0]['run_number'], x['lumi'][0]['lumi_section_num']) for x in data ]

	# datasetFileContents['/store/...'] = [(run1, lumi1), (run1, lumi2), ...]
	datasetFileContents[fileName] = sorted([str(x[0]) + ':' + str(y) for x in intermediateList for y in x[1]])

	printLock.acquire()
	progress.setPercentDone(float(i) / nFiles * 100.0)
	progress.printProgress(False)
	printLock.release()

	semaphore.release()

# greedy algorithm for finding a set covering
# https://en.wikipedia.org/wiki/Set_cover_problem#Greedy_algorithm
def set_cover(universe, subsets):
    """Find a family of subsets that covers the universal set"""
    elements = set(e for s in subsets for e in s)
    # Check the subsets cover the universe
    if elements != universe:
    	print
    	print 'elements dont cover universe???'
    	print
    	sys.exit(2)
        return None
    covered = set()
    cover = []
    # Greedily add the subsets with the most uncovered points
    while covered != elements:
        subset = max(subsets, key=lambda s: len(s - covered))
        cover.append(subset)
        covered |= subset
    return cover

def writeJSON(datasetDict, outputName):
	lumiJSON = {}
	for x in datasetDict:
		for y in datasetDict[x]:
			runNumber = str(y.split(':')[0])
			lumiNumber = int(y.split(':')[1])
			if runNumber not in lumiJSON:
				lumiJSON[runNumber] = [[lumiNumber, lumiNumber]]
			elif lumiNumber not in lumiJSON[runNumber]:
				lumiJSON[runNumber].append([lumiNumber, lumiNumber])
	with open(outputName, 'w') as outputFile:
		json.dump(lumiJSON, outputFile)

#######################################################

def doubleCheckResults():
	dataset = pickle.load(open('allFileContents_SingleMuon_bfrancis-Run2018A-17Sep2018-v2-c93e9ee70511413295b863cbd96e3fa5USER.pkl', 'rb'))
	mixed  = pickle.load(open('workspace.pkl', 'rb'))
	deletions = pickle.load(open('filesSafeToRemove.pkl', 'rb'))

	lostLumis = set()

	for f in mixed:
	        for lumi in mixed[f]:
	                wouldRemain = False
	                for otherFile in dataset:
	                        if otherFile in mixed or otherFile in deletions: continue
	                        if lumi in dataset[otherFile]:
	                                wouldRemain = True
	                                break
	                if not wouldRemain:
	                        lostLumis.add(lumi)

	print 'Deleting mixed files would lose', len(lostLumis), 'lumis'

	somethingWentWrong = False
	for f in deletions:
	        these_lumis = set(deletions[f])
	        mistakes = set()
	        for lumi in deletions[f]:
	                for otherFile in dataset:
	                        if otherFile in mixed or otherFile in deletions: continue
	                        if lumi in dataset[otherFile]:
	                                break
	                        if lumi not in lostLumis:
	                                mistakes.add(lumi)
	        if len(mistakes) > 0:
	                print 'Something went wrong with "deletable" file:', f
	                somethingWentWrong = True
	if not somethingWentWrong:
	 	print 'Deleting all filesSafeToRemove would only lose what you would lose in the mixed files.'

#######################################################
# Fill datasetFileContents with entire dataset
# datasetFileContents[file] = [(run, lumi), (run, lumi), ...]
#######################################################

if not os.path.exists('allFileContents_' + datasetLabel + '.pkl'):
	# Get the files in the dataset
	listOfFiles = subprocess.check_output('dasgoclient --query="file dataset=' + datasetName + ' instance=prod/phys03"', shell = True).split()
	if not os.path.exists('eventContentJSONs_' + datasetLabel):
		os.mkdir('eventContentJSONs_' + datasetLabel)
	print 'Running over files in dataset...'
	nFiles = len(listOfFiles)
	iFile = 0
	for x in listOfFiles:
		iFile += 1
		while active_count() > 20:
			time.sleep(1)
		threads.append(Thread(target = getLumisInFile, args = (x, iFile, nFiles)))
		threads[-1].start()
	for thread in threads:
		thread.join()
	progress.setPercentDone(100.0)
	progress.printProgress(True)

	# save a copy of datasetFileContents
	pickle.dump(datasetFileContents, open('allFileContents_' + datasetLabel + '.pkl', 'wb'))
	print '\nCreated allFileContents_' + datasetLabel + '.pkl from results in eventContentJSONs_' + datasetLabel + '/'
else:
	print '\nReading in dictionary from existing allFileContents_' + datasetLabel + '.pkl'
	datasetFileContents = pickle.load(open('allFileContents_' + datasetLabel + '.pkl', 'rb'))

#######################################################

# working copy of datasetFileContents to slim as we go
workspace = copy.deepcopy(datasetFileContents)

print '\nFinding duplicated lumis...'
allLumis = list(itertools.chain(*[x for x in workspace.values()]))
duplicateLumis = [x for x in set(allLumis) if allLumis.count(x) > 1]
print '\tFound', len(duplicateLumis), 'duplicated lumi sections!\n'

#######################################################
# first to make things easier on us, find the list of files 
# that are actually important and are solely comprised of 
# singleton lumis; ie no dupes
#######################################################

filesToKeep = {}

nPerfectFiles = 0
for x in workspace.keys():
	containsDupe = False
	for dupe in duplicateLumis:
		if dupe in workspace[x]:
			containsDupe = True
			break
	if not containsDupe:
		filesToKeep[x] = workspace.pop(x)
		nPerfectFiles += 1
print nPerfectFiles, 'files have completely unique lumi contents'

writeJSON(filesToKeep, 'keep.json')
print '\tWrote keep.json'

#######################################################

#pickle.dump(workspace, open('datasetFileContents_onlyBad.pkl', 'wb'))
#print 'Created datasetFileContents_onlyBad.pkl'

#######################################################
# second to keep making things easier on us, find any files
# that are completely contained in another file
#######################################################

filesSafeToRemove = {}
nFilesSafeToRemove = 0

f_safeToRemove = open('filesSafeToRemove.txt', 'w')
f_safeToRemove.write('Files that are safe to invalidate and delete\n\n')

nFilesSubsetsOfAnother = 0

for x in workspace.keys():
	thisLumiSet = set(workspace[x])
	for y in workspace.keys():
		if x == y:
			continue
		if thisLumiSet.issubset(set(workspace[y])):
			f_safeToRemove.write(x + '\n')
			filesSafeToRemove[x] = workspace.pop(x)
			nFilesSubsetsOfAnother += 1
			nFilesSafeToRemove += 1
			break
print '\nFind', nFilesSubsetsOfAnother, 'files that are subsets of a different file, and can be removed'

#######################################################
# we now have a mixed set of sets of lumis, and need
# to solve the set cover problem; that is, what is the
# minimal collection of files that will still provide
# every lumi?
# we do not search for an exact cover, but test if we
# found one or not; there may be duplicated lumis still
#######################################################

subsets = [set(x) for x in workspace.values()]
universe = set(list(itertools.chain(*[x for x in subsets])))
cover = set_cover(universe, subsets)

filesToCover = []

nFilesInCover = 0
nFilesNotInCover = 0

for x in workspace.keys():
	if set(workspace[x]) in cover:
		nFilesInCover += 1
	else:
		f_safeToRemove.write(x + '\n')
		filesSafeToRemove[x] = workspace.pop(x)
		nFilesNotInCover += 1
		nFilesSafeToRemove += 1
print '\nOf the remaining files,', nFilesInCover, 'provide a covering of all lumis and', nFilesNotInCover, 'can be removed'

#######################################################
# lastly find any files whose contents are all contained
# in other files; ie, it only contains duplicates
#######################################################

nFilesOnlyContainingDuplicates = 0

allLumis_remaining = list(itertools.chain(*[x for x in workspace.values()]))
duplicateLumis_remaining = [x for x in set(allLumis_remaining) if allLumis_remaining.count(x) > 1]

print '\nStill working with remaining duplicated lumis:', duplicateLumis_remaining

for fileName in workspace.keys():
	if set(workspace[fileName]).issubset(set(duplicateLumis_remaining)):
		f_safeToRemove.write(fileName + '\n')
		filesSafeToRemove[fileName] = workspace.pop(fileName)
		nFilesOnlyContainingDuplicates += 1
		nFilesSafeToRemove += 1
		# recalculate
		duplicateLumis_remaining = [x for x in set(allLumis_remaining) if allLumis_remaining.count(x) > 1]

print 'Find', nFilesOnlyContainingDuplicates, 'files that only contain duplicates, and can be removed'

#######################################################

f_safeToRemove.close()

print '\n\nIn the end, you can remove', nFilesSafeToRemove, 'files safely. See filesSafeToRemove.txt for the list.'
pickle.dump(filesSafeToRemove, open('filesSafeToRemove.pkl', 'wb'))
print '\tWrote filesSafeToRemove.pkl with their contents.'
if len(workspace) == 0:
	print '\nThere are no mixed files remaining to deal with, so this deletion does not lose any luminosity!'
else:
	print '\nThere are however', len(workspace), 'remaining files that cannot be cleanly dealt with. You can delete them, but will lose luminosity!'
	writeJSON(workspace, 'mixedFiles.json')
	pickle.dump(workspace, open('workspace.pkl', 'wb'))
	print '\tWrote mixedFiles.json and workspace.pkl with these contents'

	f_mixedFiles = open('mixedFiles.txt', 'w')
	f_mixedFiles.write('Files that have duplicated lumis, but are mixed together with unique lumis')
	f_mixedFiles.write('Deleting these are probably necessary, but a recovery CRAB job is then also necessary\n\n')
	for x in workspace:
		f_mixedFiles.write(x)
	f_mixedFiles.close()
	print '\tWrote mixedFiles.txt'

######
print '\n\nDouble checking...'
doubleCheckResults()
print '\n'