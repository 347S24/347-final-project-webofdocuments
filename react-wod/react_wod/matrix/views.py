from django.shortcuts import render, redirect
from .models import Matrix

def editor(request):
    docid = int(request.GET.get('docid', 0))
    notes = Matrix.objects.all()
 
    if request.method == 'POST':
        docid = int(request.POST.get('docid', 0))
        title = request.POST.get('title')
        documents = request.POST.get('content', '')
 
        if docid > 0:
            note = Matrix.objects.get(pk=docid)
            note.title = title
            note.documents = documents
            note.save()
 
            return redirect('/?docid=%i' % docid)
        else:
            note = Matrix.objects.create(documents=documents)
 
            return redirect('/?docid=%i' % note.id)
 
    if docid > 0:
        note = Matrix.objects.get(pk=docid)
    else:
        note = ''
 
    context = {
        'docid': docid,
        'notes': notes,
        'note': note
    }
 
    return render(request, 'node.html', context)

