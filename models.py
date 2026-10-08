from django.db import models


class Staff(models.Model):
    staffid = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=50, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    phonenumber = models.CharField(max_length=20, blank=True, null=True)
    hiredate = models.DateField(blank=True, null=True)
    mentor = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff'

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Member(models.Model):
    memberid = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=50, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    phonenumber = models.CharField(max_length=20, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    zip = models.CharField(max_length=10, blank=True, null=True)
    joindate = models.DateField(blank=True, null=True)
    isactive = models.BooleanField(default=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member'

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Asset(models.Model):
    assetid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    replacementcost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    assettype = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asset'

    def __str__(self):
        return self.title or ''


class Book(models.Model):
    asset = models.OneToOneField(Asset, models.DO_NOTHING, primary_key=True)
    isbn = models.CharField(unique=True, max_length=20, blank=True, null=True)
    pagecount = models.IntegerField(blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    genre = models.CharField(max_length=50, blank=True, null=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    publishyear = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book'

    def __str__(self):
        return self.asset.title if self.asset else ''


class Digitaldevice(models.Model):
    asset = models.OneToOneField(Asset, models.DO_NOTHING, primary_key=True)
    serialnumber = models.CharField(unique=True, max_length=50, blank=True, null=True)
    datacapgb = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    devicetype = models.CharField(max_length=50, blank=True, null=True)
    manufacturer = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'digitaldevice'

    def __str__(self):
        return f"{self.devicetype} - {self.serialnumber}"


class Copy(models.Model):
    copyid = models.IntegerField(primary_key=True)
    asset = models.ForeignKey(Asset, models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    homebranch = models.CharField(max_length=100, blank=True, null=True)
    currentlocation = models.CharField(max_length=100, blank=True, null=True)
    acquisitiondate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'copy'

    def __str__(self):
        return f"Copy {self.copyid}"


class Fineratehistory(models.Model):
    rateid = models.IntegerField(primary_key=True)
    dailyfinerate = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    effectivefrom = models.DateField(blank=True, null=True)
    effectiveto = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fineratehistory'

    def __str__(self):
        return f"Rate {self.rateid}: {self.dailyfinerate}/day"


class Loan(models.Model):
    loanid = models.IntegerField(primary_key=True)
    member = models.ForeignKey(Member, models.DO_NOTHING, blank=True, null=True)
    copy = models.ForeignKey(Copy, models.DO_NOTHING, blank=True, null=True)
    staff = models.ForeignKey(Staff, models.DO_NOTHING, blank=True, null=True)
    checkoutdate = models.DateField(blank=True, null=True)
    duedate = models.DateField(blank=True, null=True)
    returndate = models.DateField(blank=True, null=True)
    finerateattime = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loan'

    def __str__(self):
        return f"Loan {self.loanid}"


class Fine(models.Model):
    fineid = models.IntegerField(primary_key=True)
    loan = models.OneToOneField(Loan, models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    paymentstatus = models.CharField(max_length=20, default='Unpaid', blank=True, null=True)
    issueddate = models.DateField(blank=True, null=True)
    paiddate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fine'

    def __str__(self):
        return f"Fine {self.fineid} - {self.paymentstatus}"


class Meetingroom(models.Model):
    roomid = models.IntegerField(primary_key=True)
    roomname = models.CharField(max_length=50, blank=True, null=True)
    branch = models.CharField(max_length=100, blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meetingroom'

    def __str__(self):
        return self.roomname or ''


class Event(models.Model):
    eventid = models.IntegerField(primary_key=True)
    eventname = models.CharField(max_length=100, blank=True, null=True)
    eventdate = models.DateField(blank=True, null=True)
    starttime = models.TimeField(blank=True, null=True)
    endtime = models.TimeField(blank=True, null=True)
    room = models.ForeignKey(Meetingroom, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event'

    def __str__(self):
        return self.eventname or ''


class Eventparticipation(models.Model):
    event = models.OneToOneField(Event, models.DO_NOTHING, primary_key=True)
    staff = models.ForeignKey(Staff, models.DO_NOTHING, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eventparticipation'

    def __str__(self):
        return f"{self.event} - {self.staff} ({self.role})"
