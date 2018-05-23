# Generated by Django 2.0.4 on 2018-05-22 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=60)),
                ('LastName', models.CharField(max_length=60)),
                ('DOB', models.DateField()),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=7)),
                ('PhoneNumber', models.CharField(max_length=15)),
                ('Email', models.CharField(max_length=100)),
                ('FacebookID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField()),
                ('LessonDays', models.CharField(choices=[('mon', 'Mon'), ('tues', 'Tues'), ('wed', 'Wed'), ('thurs', 'Thurs'), ('fri', 'Fri'), ('sat', 'Sat'), ('sun', 'Sun')], max_length=5)),
                ('LessonTimes', models.TimeField()),
                ('LessonType', models.CharField(choices=[('acousticguitar', 'Acoustic Guitar'), ('electricguitar', 'Electric Guitar'), ('bassguitar', 'Bass Guitar'), ('piano', 'Piano'), ('cello', 'Cello'), ('drums', 'Drums'), ('violin', 'Violin'), ('saxophone', 'Saxophone'), ('harmonium', 'Harmonium'), ('tablas', 'Tablas'), ('santurs', 'Santurs'), ('vina', 'Vina')], max_length=20)),
                ('Cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='InstrumentHire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Instruments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InstrumentType', models.CharField(choices=[('acousticguitar', 'Acoustic Guitar'), ('electricguitar', 'Electric Guitar'), ('bassguitar', 'Bass Guitar'), ('piano', 'Piano'), ('cello', 'Cello'), ('drums', 'Drums'), ('violin', 'Violin'), ('saxophone', 'Saxophone'), ('harmonium', 'Harmonium'), ('tablas', 'Tablas'), ('santurs', 'Santurs'), ('vina', 'Vina')], max_length=20, verbose_name='Instrument')),
                ('HireCost', models.IntegerField()),
                ('InstrumentCondition', models.CharField(choices=[('new', 'New'), ('excellent', 'Excellent'), ('good', 'Good'), ('repair', 'Repair'), ('discard', 'Discard')], max_length=9, verbose_name='Condition')),
                ('StartDate', models.DateField(verbose_name='Start Hire')),
                ('HireLength', models.CharField(choices=[('1', '1 week'), ('2', '2 weeks'), ('3', '3 weeks'), ('4', '4 weeks'), ('5', '5 weeks'), ('6', '6 weeks'), ('7', '7 weeks'), ('8', '8 weeks')], max_length=7, verbose_name='Hire Length')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=60)),
                ('LastName', models.CharField(max_length=60)),
                ('DOB', models.DateField(default='2000-01-01')),
                ('Address', models.CharField(default='1 St', max_length=100)),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='Male', max_length=7)),
                ('PhoneNumber', models.CharField(default='0412312312', max_length=15)),
                ('Email', models.CharField(max_length=100)),
                ('FacebookID', models.IntegerField(default='1111')),
                ('TeacherInstruments', models.CharField(choices=[('acousticguitar', 'Acoustic Guitar'), ('electricguitar', 'Electric Guitar'), ('bassguitar', 'Bass Guitar'), ('piano', 'Piano'), ('cello', 'Cello'), ('drums', 'Drums'), ('violin', 'Violin'), ('saxophone', 'Saxophone'), ('harmonium', 'Harmonium'), ('tablas', 'Tablas'), ('santurs', 'Santurs'), ('vina', 'Vina')], max_length=20, verbose_name='Instrument')),
                ('LessonDays', models.CharField(choices=[('mon', 'Mon'), ('tues', 'Tues'), ('wed', 'Wed'), ('thurs', 'Thurs'), ('fri', 'Fri'), ('sat', 'Sat'), ('sun', 'Sun')], max_length=5, verbose_name='Day')),
                ('LessonTime', models.CharField(choices=[('7', '7am'), ('8', '8am'), ('9', '9am'), ('10', '10am'), ('11', '11am'), ('12', '12pm'), ('13', '1pm'), ('14', '2pm'), ('15', '3pm'), ('16', '4pm'), ('17', '5pm'), ('18', '6pm'), ('19', '7pm')], max_length=13, verbose_name='Time')),
                ('TeacherLanguageSkills', models.CharField(choices=[('english', 'English'), ('chinese', 'Chinese'), ('spanish', 'Spanish'), ('hindi', 'Hindi'), ('arabic', 'Arabic'), ('portuguese', 'Portuguese'), ('bengali', 'Bengali'), ('russian', 'Russian'), ('japanese', 'Japanese'), ('punjabi', 'Punjabi')], max_length=10, verbose_name='Language')),
                ('TeacherGender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=7, verbose_name='Teacher Gender')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InstrumentSkill', models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=1)),
                ('LanguageSkill', models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=1)),
                ('TeachingSkill', models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=1)),
                ('FeedbackComment', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=60)),
                ('LastName', models.CharField(max_length=60)),
                ('DOB', models.DateField()),
                ('Qualifications', models.CharField(max_length=100)),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=7)),
                ('PhoneNumber', models.CharField(max_length=15)),
                ('Email', models.CharField(max_length=100)),
                ('FacebookID', models.IntegerField()),
                ('Instruments', models.CharField(choices=[('acousticguitar', 'Acoustic Guitar'), ('electricguitar', 'Electric Guitar'), ('bassguitar', 'Bass Guitar'), ('piano', 'Piano'), ('cello', 'Cello'), ('drums', 'Drums'), ('violin', 'Violin'), ('saxophone', 'Saxophone'), ('harmonium', 'Harmonium'), ('tablas', 'Tablas'), ('santurs', 'Santurs'), ('vina', 'Vina')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TeachingSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TeachingDays', models.CharField(choices=[('mon', 'Mon'), ('tues', 'Tues'), ('wed', 'Wed'), ('thurs', 'Thurs'), ('fri', 'Fri'), ('sat', 'Sat'), ('sun', 'Sun')], max_length=5)),
                ('StartTime', models.CharField(choices=[('7', '7am'), ('8', '8am'), ('9', '9am'), ('10', '10am'), ('11', '11am'), ('12', '12pm'), ('13', '1pm'), ('14', '2pm'), ('15', '3pm'), ('16', '4pm'), ('17', '5pm'), ('18', '6pm'), ('19', '7pm')], max_length=13)),
                ('ScheduleStatus', models.CharField(choices=[('full', 'Full'), ('empty', 'Empty')], max_length=4)),
                ('Teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Teachers')),
            ],
        ),
        migrations.AddField(
            model_name='teacherfeedback',
            name='Teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Teachers'),
        ),
        migrations.AddField(
            model_name='instrumenthire',
            name='Instrument',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Instruments'),
        ),
        migrations.AddField(
            model_name='instrumenthire',
            name='Student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Students'),
        ),
        migrations.AddField(
            model_name='contract',
            name='Student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Students'),
        ),
        migrations.AddField(
            model_name='contract',
            name='Teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Teachers'),
        ),
    ]
