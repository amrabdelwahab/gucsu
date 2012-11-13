# Create your views here.
import os
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django import http
from candidates.models import Faculty,Committee,CabinetPosition,PresidentialCabinet,Batch,SJBCandidate,SenateCandidate,ScCandidate,AcCandidate,PresidentialCabinetMember
from django.template import RequestContext, loader

def index(request):
    return render_to_response('index.html',{})

def nominateindex(request):
    return render_to_response('nominateindex.html',{})

def sjbindex(request):
    return render_to_response('sjbindex.html',{})
def senateindex(request):
    return render_to_response('senateindex.html',{})
def scindex(request):
    return render_to_response('scindex.html',{})
def prindex(request):
    return render_to_response('prindex.html',{})
def viewindex(request):
    #candidate=SJBCandidate.objects.get(pk=1)
    #img=os.path.basename(candidate.image.name)
    faculties=Faculty.objects.all()
    committees=Committee.objects.all()
    cabinets=PresidentialCabinet.objects.all()
    return render_to_response('viewindex.html',{'faculties':faculties, 'committees' : committees, 'cabinets' : cabinets},
                              context_instance=RequestContext(request))


def nominateSJB(request):
    if request.method=='POST':
        tmpname=request.POST['name']
        tmpid=request.POST['id']
        tmpmobile=request.POST['mobile']
        tmpgpa=request.POST['gpa']
        tmpmail=request.POST['mail']
        tmpfile=request.FILES['file']
        tmpagenda=request.POST['agenda']
        tmpfaculty=Faculty.objects.get(pk=request.POST.get('faculty'))
	tmpbatch=Batch.objects.get(pk=request.POST.get('batch'))
        candidate=SJBCandidate.objects.create(name=tmpname,studentID=tmpid,faculty=tmpfaculty,batch=tmpbatch,image=tmpfile,mobile=tmpmobile,GUCemail=tmpmail, GPA=tmpgpa,agenda=tmpagenda)
        candidate.save()
	return HttpResponseRedirect('/')
    else:
	batches=Batch.objects.all()
	faculties=Faculty.objects.all()
	return render_to_response('nominatesjb.html', context_instance=RequestContext(request,{ 'batches' : batches,'faculties': faculties}))
def nominateSenate(request):
    if request.method=='POST':
        tmpname=request.POST['name']
        tmpid=request.POST['id']
        tmpmobile=request.POST['mobile']
        tmpgpa=request.POST['gpa']
        tmpmail=request.POST['mail']
        tmpfile=request.FILES['file']
        tmpagenda=request.POST['agenda']
        tmpfaculty=Faculty.objects.get(pk=request.POST.get('faculty'))
	tmpbatch=Batch.objects.get(pk=request.POST.get('batch'))
        candidate=SenateCandidate.objects.create(name=tmpname,studentID=tmpid,faculty=tmpfaculty,batch=tmpbatch,image=tmpfile,mobile=tmpmobile,GUCemail=tmpmail, GPA=tmpgpa,agenda=tmpagenda)
        candidate.save()
	return HttpResponseRedirect('/')
    else:
	batches=Batch.objects.all()
	faculties=Faculty.objects.all()
	return render_to_response('nominatesenate.html', context_instance=RequestContext(request,{ 'batches' : batches,'faculties': faculties}))
def newpc(request):
    if request.method=='POST':
	tmpagenda=request.POST['agenda']
        cabinet=PresidentialCabinet.objects.create(name=request.POST['cname'],agenda=tmpagenda,SecretCode=request.POST['key'])
	cabinet.save()
        tmpname=request.POST['name']
        tmpid=request.POST['id']
        tmpmobile=request.POST['mobile']
        tmpgpa=request.POST['gpa']
        tmpmail=request.POST['mail']
        tmpfile=request.FILES['file']
        tmpfaculty=Faculty.objects.get(pk=request.POST.get('faculty'))
	tmpbatch=Batch.objects.get(pk=request.POST.get('batch'))
	pres=CabinetPosition.objects.get(pk=1)
	ag=""
        candidate=PresidentialCabinetMember.objects.create(agenda=ag,cabinet=cabinet,position=pres,name=tmpname,studentID=tmpid,faculty=tmpfaculty,batch=tmpbatch,image=tmpfile,mobile=tmpmobile,GUCemail=tmpmail, GPA=tmpgpa)
        candidate.save()
	return HttpResponseRedirect('/')
    else:
	batches=Batch.objects.all()
	faculties=Faculty.objects.all()
	return render_to_response('newpc.html', context_instance=RequestContext(request,{ 'batches' : batches,'faculties': faculties}))
def join(request):
    if request.method=='POST':
	cabinet=PresidentialCabinet.objects.get(pk=request.POST.get('cab'))
	if cabinet.SecretCode==request.POST['key']:
		tmpname=request.POST['name']
        	tmpid=request.POST['id']
        	tmpmobile=request.POST['mobile']
        	tmpgpa=request.POST['gpa']
        	tmpmail=request.POST['mail']
        	tmpfile=request.FILES['file']
        	tmpfaculty=Faculty.objects.get(pk=request.POST.get('faculty'))
		tmpbatch=Batch.objects.get(pk=request.POST.get('batch'))
		pos=CabinetPosition.objects.get(pk=request.POST.get('pos'))
		ag=""
        	candidate=PresidentialCabinetMember.objects.create(agenda=ag,cabinet=cabinet,position=pos,name=tmpname,studentID=tmpid,faculty=tmpfaculty,batch=tmpbatch,image=tmpfile,mobile=tmpmobile,GUCemail=tmpmail, GPA=tmpgpa)
        	candidate.save()
		return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')		
    else:
	batches=Batch.objects.all()
	faculties=Faculty.objects.all()
	positions=CabinetPosition.objects.all()
	cabinets=PresidentialCabinet.objects.all()
	return render_to_response('join.html', context_instance=RequestContext(request,{'positions':positions,'cabinets':cabinets, 'batches' : batches,'faculties': faculties}))

def show(request):
    if request.method=='POST':
	post=request.POST.get('post')
	if post == 'PC':
		cabinet=PresidentialCabinet.objects.get(pk=request.POST.get('cab'))
		cabinetmembers=PresidentialCabinetMember.objects.filter(cabinet=cabinet)
		return render_to_response('ViewPC.html', context_instance=RequestContext(request,{'cabinetmembers':cabinetmembers,'cabinet':cabinet}))
	if post == 'SJB':
		faculty=Faculty.objects.get(pk=request.POST.get('faculty'))
		candidates=SJBCandidate.objects.filter(faculty=faculty)
		return render_to_response('ViewSJB.html', context_instance=RequestContext(request,{'candidates':candidates,'faculty':faculty}))
	if post == 'Senate':
		faculty=Faculty.objects.get(pk=request.POST.get('faculty'))
		candidates=SenateCandidate.objects.filter(faculty=faculty)
		return render_to_response('ViewSenate.html', context_instance=RequestContext(request,{'candidates':candidates,'faculty':faculty}))
	if post == 'SC':
		faculty=Faculty.objects.get(pk=request.POST.get('faculty'))
		if request.POST.get('committee')=='1':
			grade=request.POST.get('grade')
			candidates=AcCandidate.objects.filter(faculty=faculty,grade=request.POST.get('grade'))
			return render_to_response('ViewAC.html', context_instance=RequestContext(request,{'candidates':candidates,'faculty':faculty,'grade' :grade}))

		else:
			committee=Committee.objects.get(pk=request.POST.get('committee'))
			candidates=ScCandidate.objects.filter(faculty=faculty,committee=committee)
			return render_to_response('ViewSC.html', context_instance=RequestContext(request,{'candidates':candidates,'faculty':faculty, 'committee': committee}))

def nominateSC(request):
    if request.method=='POST':
        tmpname=request.POST['name']
        tmpid=request.POST['id']
        tmpmobile=request.POST['mobile']
        tmpgpa=request.POST['gpa']
        tmpmail=request.POST['mail']
        tmpfile=request.FILES['file']
        tmpagenda=request.POST['agenda']
	tmpgrade=request.POST['grade']
        tmpfaculty=Faculty.objects.get(pk=request.POST.get('faculty'))
	tmpbatch=Batch.objects.get(pk=request.POST.get('batch'))
        tmpcom=Committee.objects.get(pk=request.POST.get('com'))
	if tmpcom.id==1:
        	candidate=AcCandidate.objects.create(name=tmpname,studentID=tmpid,faculty=tmpfaculty,batch=tmpbatch,grade=tmpgrade,image=tmpfile,mobile=tmpmobile,GUCemail=tmpmail, GPA=tmpgpa,agenda=tmpagenda)
        	candidate.save()
	else:
        	candidate=ScCandidate.objects.create(name=tmpname,studentID=tmpid,committee=tmpcom,faculty=tmpfaculty,batch=tmpbatch,image=tmpfile,mobile=tmpmobile,GUCemail=tmpmail, GPA=tmpgpa,agenda=tmpagenda)
        	candidate.save()
	return HttpResponseRedirect('/')
    else:
	batches=Batch.objects.all()
	faculties=Faculty.objects.all()
	committees=Committee.objects.all()
	return render_to_response('nominateSC.html', context_instance=RequestContext(request,{ 'batches' : batches,'committees' : committees,'faculties': faculties}))

