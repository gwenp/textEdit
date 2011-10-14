import gtk

class MainMenuBar(gtk.MenuBar):
	def __init__(self,wTree):
		self = wTree.get_widget("mainMenuBar")
		self.menuItem_newFile = wTree.get_widget("menuItem_newFile")
		self.menuItem_openFile = wTree.get_widget("menuItem_openFile")
		self.menuItem_quit = wTree.get_widget("menuItem_quit")
		
		self.menuItem_quit.connect("activate", gtk.main_quit)
