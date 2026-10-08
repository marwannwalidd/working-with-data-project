from django.shortcuts import render, get_object_or_404
from .models import Member, Loan, Fine, Book, Staff, Event, Copy, Asset, Digitaldevice, Meetingroom


def home(request):
    context = {
        'total_members': Member.objects.count(),
        'total_loans': Loan.objects.count(),
        'active_loans': Loan.objects.filter(returndate__isnull=True).count(),
        'unpaid_fines': Fine.objects.filter(paymentstatus='Unpaid').count(),
        'total_staff': Staff.objects.count(),
        'total_books': Book.objects.count(),
        'upcoming_events': Event.objects.order_by('eventdate')[:3],
        'recent_loans': Loan.objects.select_related('member', 'copy').order_by('-loanid')[:5],
    }
    return render(request, 'library/home.html', context)


def members(request):
    search = request.GET.get('search', '')
    all_members = Member.objects.all().order_by('memberid')
    if search:
        all_members = all_members.filter(firstname__icontains=search) | \
                      all_members.filter(lastname__icontains=search) | \
                      all_members.filter(email__icontains=search)
    return render(request, 'library/members.html', {'members': all_members, 'search': search})


def loans(request):
    filter_type = request.GET.get('filter', 'active')
    if filter_type == 'all':
        loans_qs = Loan.objects.select_related('member', 'copy', 'copy__asset').order_by('-loanid')
    elif filter_type == 'returned':
        loans_qs = Loan.objects.filter(returndate__isnull=False).select_related('member', 'copy', 'copy__asset').order_by('-loanid')
    else:
        loans_qs = Loan.objects.filter(returndate__isnull=True).select_related('member', 'copy', 'copy__asset').order_by('-loanid')
    return render(request, 'library/loans.html', {'loans': loans_qs, 'filter_type': filter_type})


def fines(request):
    filter_status = request.GET.get('status', 'all')
    all_fines = Fine.objects.select_related('loan', 'loan__member').order_by('-fineid')
    if filter_status == 'unpaid':
        all_fines = all_fines.filter(paymentstatus='Unpaid')
    elif filter_status == 'paid':
        all_fines = all_fines.filter(paymentstatus='Paid')
    return render(request, 'library/fines.html', {'fines': all_fines, 'filter_status': filter_status})


def books(request):
    search = request.GET.get('search', '')
    all_books = Book.objects.select_related('asset').order_by('asset__title')
    if search:
        all_books = all_books.filter(author__icontains=search) | \
                    all_books.filter(asset__title__icontains=search) | \
                    all_books.filter(genre__icontains=search)
    return render(request, 'library/books.html', {'books': all_books, 'search': search})


def events(request):
    all_events = Event.objects.select_related('room').order_by('eventdate')
    return render(request, 'library/events.html', {'events': all_events})


def staff(request):
    all_staff = Staff.objects.all().order_by('staffid')
    return render(request, 'library/staff.html', {'staff': all_staff})


def devices(request):
    all_devices = Digitaldevice.objects.select_related('asset').order_by('asset__title')
    return render(request, 'library/devices.html', {'devices': all_devices})
