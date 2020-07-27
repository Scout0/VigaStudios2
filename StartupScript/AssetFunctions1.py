
import unreal
import os

#import AssetFunctions1 as AF
#reload(AF)
#AF.importMyAssets()


default_address_tga = 'D:/UE4 Folders/VIGAfiles/Assets/tga/'
default_address_wav = 'D:/UE4 Folders/VIGAfiles/Assets/wav/'

def findTGAFolder(address = default_address_tga):
	ourFolder = os.listdir(address)
	for ourFile in ourFolder:
		texture_tga = address + ourFile 
		importMyAssetsTGA(texture_tga)
	
def findWAVFolder(address = default_address_wav):
	ourFolder = os.listdir(address)
	for ourFile in ourFolder:
		sound_wav = address + ourFile 
		importMyAssetsWAV(sound_wav)
	
def importMyAssetsTGA(texture_tga):
	texture_task = buildImportTask(texture_tga, '/Game/Textures')
	executeImportTasks([texture_task])

def importMyAssetsWAV(sound_wav):
	sound_task = buildImportTask(sound_wav, '/Game/Sounds')
	executeImportTasks([sound_task])

def buildImportTask(filename, destination_path):
	task = unreal.AssetImportTask()
	task.set_editor_property('automated', True)
	task.set_editor_property('destination_name', '')
	task.set_editor_property('destination_path', destination_path)
	task.set_editor_property('filename', filename)
	task.set_editor_property('replace_existing', True)
	task.set_editor_property('save', True)
	return task

def executeImportTasks(tasks):
	unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)
	for task in tasks:
		for path in task.get_editor_property('imported_object_paths'):
			print('Imported: %s' % path)
