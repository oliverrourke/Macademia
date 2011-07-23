# python manage.py sql documents
# python manage.py syncdb
# python manage.py runserver
# python manage.py collectstatic
# python manage.py flush

#python manage.py reset documents

# python manage.py shell


from documents.models import Folder, File
Folder.objects.all()
p = Folder(name = 'Home', parent_folder = -1, folder_path = 'Home')
p.save()



from documents.models import File
a = File(file_name = 'blah.txt', file_path = 'blah.txt', parent_folder = 1, created_on = '2011-1-1 12:00', created_by = 1, last_updated_on = '2011-1-1 12:00', last_updated_by = 1)

a = File(created_by = 1)


import cStringIO

output = cStringIO.StringIO()
output.write('First line.\n')
output.close()
"""

Thoughts
Comments on comments -indented, collapsible. Email notifications?
Categories of comments - when posting comment add checkbox (eg. to do). User created categories

Underneath much like google docs - each user can have a series of documents which they can access and can allow other people to access and or edit etc. Documents can be classified into folders or tagged as in google docs - eg. might include code, published papers, drafts etc etc. As of yet I see no real need to distinguish between these categories, can leave it up to users to create them as needed.

Unlike general public, academics on the whole do not care for presentation too much at preparation stage - as long as it is easy to read (syntactical coloring for code etc, probably best done piggy backing off some public domain software someware), they are more than happy. For files which can't/won't be edited in place, include simple steps to update files online.

 Include version control on all documents.



Key difference from google docs is the emphasis from individuals to research teams and research spaces - a space can exist as its own entity independent from any users (although of course administrator(s) for each space would be required). Any members of a team can contribute documents/comments etc to a research space, which will remain in said research space even if creating member leaves team. Adding/removing a user to a team should be quick - no need to set permission on all files/folders relevant to team.

Include the ability for users with read privileges to comment on docs. These comments need to be more than just a bubble/idea etc - this is where the majority of research actually happens. Make comments easy to search (by date/user/topic/section of document), and allow users to reference other documents in comments through one click shortcuts - this will facilitate sharing of subroutines/sections in drafts as well as providing references for works in progress. 

Make adding shortcuts easy, for example through simple code words, eg. typing \papers{Fontana 09} would search in papers folder for all files which are similar to Fontana 09, causing a drop down menu to appear in real time which can be tabbed through to select appropriate file (or add another button which allows slower addition of shortcut via a folders/checkbox display). Adding tags must be very simple and fast. 

Add functionality to allow viewing of files depending on if/where they have been tagged. Eg. can pull up lists of all papers which were referenced in certain draft of paper.

Include the ability for easy sharing of documents in team space by any member of research team through https: address, with option of including comments etc. - however anyone outside team will only be able to access those documents which they have been sent the address for, and all other documents in space will not be reachable. Those not in the team would normally have no commenting/editing privileges (although could be bestowed if desired).

Ideally all of this could be done on two levels - online interface and command line as many still prefer working on command line. Not sure how this might be achieved.

"""