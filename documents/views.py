from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from models import Folder, File, Comment
from folder_processing_functions import Address, add_comment, upload_file, remove_folder

def main(request, rest_of_address):
	address = Address(rest_of_address)
	#import pdb; pdb.set_trace()
	if not address.folder:
		return render_to_response('documents_folders/error.html', {'error':'no_folder', 'current_folder_path': address.folder_path})
	if address.file_path and not address.file:
		return render_to_response('documents_folders/error.html', {'error':'no_file', 'current_folder': address.folder_path, 'open_file':address.file_path})
	if 'submit_comment' in request.POST: 
		add_comment(request, address)
	#Create new folder
	if 'file' in request.FILES:
		upload_file(request, address.folder.id)
	if 'new_folder_name' in request.POST:
		folder_name = str(request.POST.get('new_folder_name'))
		if folder_name.strip():
			p = Folder(name = folder_name, parent_folder = address.folder.id, folder_path = address.folder_path+'/'+folder_name)
			p.save()
	#Remove folder and all sub-folders of that folder
	for folder_id in [a for a, b in request.POST.iteritems() if b == 'Delete']:
		remove_folder(folder_id)
	sub_folders = Folder.objects.filter(parent_folder=address.folder.id)
	sub_files = File.objects.filter(parent_folder = address.folder.id)
	relevant_comments = Comment.objects.filter(attached_to_type = address.type, attached_to_id = address.id)
	try:
		parent_folder = Folder.objects.get(id = address.folder.parent_folder)
	except:
		parent_folder = None
	return render_to_response('documents_folders/blah.html', {'relevant_comments':relevant_comments, 'sub_folders': sub_folders, 'current_folder_path': address.folder.folder_path, 'parent_folder': parent_folder, 'sub_files':sub_files, 'open_file':address.file_path, 'current_path': '/documents/'+rest_of_address}, context_instance=RequestContext(request))
		
def files(request, file_name):
	return render_to_response('documents_files/file.html', {'file_name': file_name})