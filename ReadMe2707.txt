VIGA Studios Plugin - Direct installation in UE from a given url.


Steps to install Plugin in project - 
1. Copy Plugin folder inside "Plugin" of your project
2. Open Project
3. Enable "Editor Scripting Utilities" and "Python Editor Script Plugin" in Plugins
4. Go to Project Settings -> Python -> 
	a. Enable Develper Mode
	b. In "Additional Paths", after going inside your project folder, browse to 
		Plugins -> Plugin Name -> Select Folder "StartupScript"
   and restart the editor.
5. In the Content Browser, go to Viga7Plugin0907Content,
   Right click "Viga7EditorUtilityWidget" -> Run Editor Utility Widget
   
How to use the plugin- 
1. Make a folder with the path - D:/Temp/
   Files will be downloaded here and then deleted.
2. Input should be inserted in this format : 'http://127.0.0.1:800/filenameInTheServer.fbx'
	e.g. 'http://127.0.0.1:8000/ib1.fbx'
