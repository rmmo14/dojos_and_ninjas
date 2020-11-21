
# List of Query commands
## Query: Create 3 new dojos
>>> Dojo.objects.create(name="Furst", city="Austin", state="TX")
<Dojo: Dojo object (1)>
>>> Dojo.objects.create(name="Sekond", city="Chicago", state="IL")
<Dojo: Dojo object (2)>
>>> Dojo.objects.create(name="Thurt", city="Sacramento", state="CA")
<Dojo: Dojo object (3)>

## Query: Delete the 3 dojos created
>>> c = Dojo.objects.get(id=3)
>>> c.delete()
(1, {'dojosninjas_app.Ninja': 0, 'dojosninjas_app.Dojo': 1})
>>> Dojo.objects.all()
<QuerySet [<Dojo: Dojo object (1)>, <Dojo: Dojo object (2)>]>
>>> m = Dojo.objects.get(id=2)
>>> m.delete()
(1, {'dojosninjas_app.Ninja': 0, 'dojosninjas_app.Dojo': 1})
>>> n=Dojo.objects.get(id=1)
>>> n.delete()
(1, {'dojosninjas_app.Ninja': 0, 'dojosninjas_app.Dojo': 1})
>>> Dojo.objects.all()
<QuerySet []>

## Query: Create 3 more dojos
>>> Dojo.objects.create(name="Fourth", city = "Bell", state="CA")
<Dojo: Dojo object (4)>
>>> Dojo.objects.all()
<QuerySet [<Dojo: Dojo object (4)>]>
>>> Dojo.objects.first()
<Dojo: Dojo object (4)>
>>> Dojo.objects.create(name="Fifth", city="Cudahy", state="CA")
<Dojo: Dojo object (5)>
>>> Dojo.objects.create(name="Sixth", city="Eugene", state="OR")
<Dojo: Dojo object (6)>

## Create 3 ninjas that belong to the first dojo

>>> firstdojo = Dojo.objects.get(id=4)
>>> stud1forfirst = Ninja.objects.create(first_name="Abe", last_name="Banana", dojo_id = firstdojo)
>>> stud2forfirst = Ninja.objects.create(first_name="Cookie", last_name="Diggum", dojo_id = firstdojo)
>>> stud3forfirst = Ninja.objects.create(first_name="Edify", last_name="Flank", dojo_id = firstdojo)

## Create 3 ninjas that belong to the second dojo

>>> seconddojo = Dojo.objects.get(id=5)
>>> stud1forsecond = Ninja.objects.create(first_name="Gessi", last_name="Hip", dojo_id = seconddojo)
>>> stud2forsecond = Ninja.objects.create(first_name="Ignis", last_name="Jayke", dojo_id = seconddojo)
>>> stud3forsecond = Ninja.objects.create(first_name="Kilt", last_name="Lork", dojo_id = seconddojo)

## Create 3 ninjas that belong to the third dojo

>>> thirddojo = Dojo.objects.get(id=6)
>>> stud1forthird= Ninja.objects.create(first_name="Maizy", last_name="Nounce", dojo_id=thirddojo)
>>> stud2forthird= Ninja.objects.create(first_name="Otty", last_name="Pluss", dojo_id=thirddojo)
>>> stud3forthird= Ninja.objects.create(first_name="Quince", last_name="Reik", dojo_id=thirddojo)

## Retrieve all the ninjas from the first dojo
>>> firstdojo.ninjas.all()
<QuerySet [<Ninja: Ninja object (1)>, <Ninja: Ninja object (2)>, <Ninja: Ninja object (3)>]>

## Retrieve all the ninjas from the last dojo
>>> thirddojo.ninjas.all()
<QuerySet [<Ninja: Ninja object (7)>, <Ninja: Ninja object (8)>, <Ninja: Ninja object (9)>]>

## Retrieve the last ninjas dojo
>>> thirddojo.ninjas.last().dojo_id
<Dojo: Dojo object (6)>

## add a new field to Dojo class and create a new dojo with it

(djangoPy3Env) renemontoya@Renes-Air dojosninjas_proj % python manage.py makemigrations
You are trying to add a non-nullable field 'desc' to dojo without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 1  
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> ""
Migrations for 'dojosninjas_app':
  dojosninjas_app/migrations/0002_dojo_desc.py
(djangoPy3Env) renemontoya@Renes-Air dojosninjas_proj % python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, dojosninjas_app, sessions
Running migrations:
  Applying dojosninjas_app.0002_dojo_desc... OK
  >>> from dojosninjas_app.models import *
>>> Dojo.objects.create(name = "se7en", city ="San Antonio", state ="TX", desc = "a sample of texas")
<Dojo: Dojo object (7)>