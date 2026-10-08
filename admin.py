from django.contrib import admin
from .models import (Staff, Member, Asset, Book, Digitaldevice,
                     Copy, Loan, Fine, Meetingroom, Event, Eventparticipation, Fineratehistory)


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('staffid', 'firstname', 'lastname', 'position', 'email', 'hiredate')
    search_fields = ('firstname', 'lastname', 'email', 'position')
    list_filter = ('position',)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('memberid', 'firstname', 'lastname', 'email', 'city', 'joindate', 'isactive')
    search_fields = ('firstname', 'lastname', 'email')
    list_filter = ('isactive', 'city')


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('assetid', 'title', 'assettype', 'replacementcost')
    list_filter = ('assettype',)
    search_fields = ('title',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('asset', 'isbn', 'author', 'genre', 'publisher', 'publishyear', 'pagecount')
    search_fields = ('author', 'isbn', 'genre')
    list_filter = ('genre', 'publishyear')


@admin.register(Digitaldevice)
class DigitaldeviceAdmin(admin.ModelAdmin):
    list_display = ('asset', 'serialnumber', 'devicetype', 'manufacturer', 'datacapgb')
    search_fields = ('serialnumber', 'manufacturer', 'devicetype')


@admin.register(Copy)
class CopyAdmin(admin.ModelAdmin):
    list_display = ('copyid', 'asset', 'status', 'homebranch', 'currentlocation', 'acquisitiondate')
    list_filter = ('status', 'homebranch')
    search_fields = ('homebranch',)


@admin.register(Fineratehistory)
class FineratehistoryAdmin(admin.ModelAdmin):
    list_display = ('rateid', 'dailyfinerate', 'effectivefrom', 'effectiveto')


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('loanid', 'member', 'copy', 'staff', 'checkoutdate', 'duedate', 'returndate')
    list_filter = ('checkoutdate', 'duedate')
    search_fields = ('member__firstname', 'member__lastname')


@admin.register(Fine)
class FineAdmin(admin.ModelAdmin):
    list_display = ('fineid', 'loan', 'amount', 'paymentstatus', 'issueddate', 'paiddate')
    list_filter = ('paymentstatus',)


@admin.register(Meetingroom)
class MeetingroomAdmin(admin.ModelAdmin):
    list_display = ('roomid', 'roomname', 'branch', 'capacity')
    list_filter = ('branch',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('eventid', 'eventname', 'eventdate', 'starttime', 'endtime', 'room')
    list_filter = ('eventdate',)
    search_fields = ('eventname',)


@admin.register(Eventparticipation)
class EventparticipationAdmin(admin.ModelAdmin):
    list_display = ('event', 'staff', 'role')
    list_filter = ('role',)
