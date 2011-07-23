from models import Folder, File, Comment

def extract_folder_file(extra_information):
	cut = extra_information.find('&file=')
	if cut == -1:
		current_folder_path = extra_information
		open_file = ''
	else:
		current_folder_path=extra_information[:cut]
		open_file=extra_information[cut+6:]
	return current_folder_path, open_file

class Address:
	def __init__(self, rest_of_address):
		cut = rest_of_address.find('&file=')
		if cut == -1:
			self.folder_path = str(rest_of_address)
			self.file_path = ''
		else:
			self.folder_path = str(rest_of_address[:cut])
			self.file_path = str(rest_of_address[cut+6:])
			
		try: self.folder = Folder.objects.get(folder_path = self.folder_path)
		except: self.folder = None
		
		try: self.file = File.objects.get(file_path = self.file_path)
		except: self.file = None
		
		if self.file:
			self.type = 1
			self.id = self.file.id
		elif self.folder:
			self.type = 0
			self.id = self.folder.id

def add_comment(self, request, address):
	if request.POST['comment']:
		c = Comment(content = request.POST['comment'], created_by = 1, created_on = '2011-1-1 12:00', attached_to_type = address.type, attached_to_id = address.id)
		c.save()
		
def upload_file(request, folder_id):
	#import pdb; pdb.set_trace()
	if request.method=='POST':
		handle_uploaded_file(request.FILES['file'], request.FILES['file'].name)		
		f = File(file_name = request.FILES['file'].name, file_path = request.FILES['file'].name, parent_folder = folder_id, created_on = '2011-1-1 12:00', created_by = 1, last_updated_on = '2011-1-1 12:00', last_updated_by = 1)
		f.save()
		
def handle_uploaded_file(f, name):
    destination = open('/Users/Oliver/Documents/macademia/media/'+name, 'w+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()

def remove_folder(folder_id):
	folders_to_be_deleted = [x for x in Folder.objects.filter(parent_folder=folder_id)]
	folders_to_be_deleted.append(Folder.objects.get(pk=folder_id))
	#import pdb; pdb.set_trace()
	while folders_to_be_deleted:
		folder = folders_to_be_deleted.pop()
		folders_to_be_deleted.extend([x for x in Folder.objects.filter(parent_folder=lower_folder.id)])
		#remove_files(folder.id)
		#remove_comments(0, folder.id)
		folder.delete()

#def remove_file()