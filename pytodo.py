import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf

class ToDoApp(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="PyToDo")
		self.set_border_width(10)
		self.set_default_size(480, 640)

		# Set app icon
		icon = GdkPixbuf.Pixbuf.new_from_file("pytodo.png")
		self.set_icon(icon)

		# Main layout
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.add(vbox)

		# Menu Bar
		menubar = Gtk.MenuBar()
		vbox.pack_start(menubar, False, False, 0)

		# File menu
		filemenu = Gtk.Menu()
		fileitem = Gtk.MenuItem(label="File")
		fileitem.set_submenu(filemenu)
		menubar.append(fileitem)

		# Save menu item (dummy)
		save_item = Gtk.MenuItem(label="Save")
		save_item.connect("activate", self.on_save)
		filemenu.append(save_item)

		# Exit menu item
		exit_item = Gtk.MenuItem(label="Exit")
		exit_item.connect("activate", self.on_exit)
		filemenu.append(exit_item)

		# Help menu
		helpmenu = Gtk.Menu()
		helpitem = Gtk.MenuItem(label="Help")
		helpitem.set_submenu(helpmenu)
		menubar.append(helpitem)

		# About menu item
		about_item = Gtk.MenuItem(label="About")
		about_item.connect("activate", self.on_about)
		helpmenu.append(about_item)

		# Scrolled window
		scrolled_window = Gtk.ScrolledWindow()
		scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
		vbox.pack_start(scrolled_window, True, True, 0)

		# Task list inside scrolled window
		self.todo_list = Gtk.ListBox()
		scrolled_window.add(self.todo_list)

		# Entry field for new tasks
		self.entry = Gtk.Entry()
		vbox.pack_start(self.entry, False, False, 0)

		# Add task button
		self.add_button = Gtk.Button(label="Add Task")
		self.add_button.connect("clicked", self.add_task)
		vbox.pack_start(self.add_button, False, False, 0)

	def add_task(self, widget):
		task_text = self.entry.get_text()
		if task_text:
			todo_row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
			todo_label = Gtk.Label(label=task_text)
			todo_row.pack_start(todo_label, True, True, 0)

			# Mark as Complete button
			complete_button = Gtk.Button(label="Complete")
			complete_button.connect("clicked", self.complete_task, todo_label)
			todo_row.pack_start(complete_button, False, False, 0)

			# Delete button
			delete_button = Gtk.Button(label="Delete")
			delete_button.connect("clicked", self.delete_task, todo_row)
			todo_row.pack_start(delete_button, False, False, 0)

			self.todo_list.add(todo_row)
			self.todo_list.show_all()
			self.entry.set_text("")
			self.entry.grab_focus()

	def complete_task(self, widget, todo_label):
		todo_label.set_markup(f"<s>{todo_label.get_text()}</s>")

	def delete_task(self, widget, todo_row):
		parent = todo_row.get_parent()
		if parent:
			self.todo_list.remove(parent)

	def on_exit(self, widget):
		Gtk.main_quit()

	def on_about(self, widget):
		about_dialog = Gtk.AboutDialog()
		about_dialog.set_program_name("PyToDo")
		about_dialog.set_authors(["Ricardo1pran"])
		about_dialog.set_logo(GdkPixbuf.Pixbuf.new_from_file("pytodo.png"))
		about_dialog.run()
		about_dialog.destroy()

	def on_save(self, widget):
		dialog = Gtk.MessageDialog(
			transient_for=self,
			flags=0,
			message_type=Gtk.MessageType.INFO,
			buttons=Gtk.ButtonsType.OK,
			text="Feature is Coming!",
		)
		dialog.format_secondary_text(
			"This feature is under development. Stay tuned!"
		)
		dialog.run()
		dialog.destroy()

win = ToDoApp()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
