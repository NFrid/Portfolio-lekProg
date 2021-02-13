# ВСР 3. Задание: разработать прототип приложения «Регистрация на
# конференциюю на основе фрагмента технического задания
# с использованием ООП.


import re


class Registration:
    def __init__(self):
        self.__fname = ""
        self.__sname = ""
        self.__email = ""
        self.__affiliation = ""
        self.__year = ""
        self.__country = ""
        self.__city = ""
        self.__presentation = 0
        self.__emaildist = False
        self.__postal = ""
        self.__adress = ""
        self.__sourceinfo = ""
        self.__typeofreg = ""
        self.__comment = ""

    def new(
        self,
        fname,
        sname,
        email,
        affil,
        year,
        country,
        city,
        pres,
        emaildist,
        postal=None,
        adress=None,
        sourceinfo=None,
        typeofreg=None,
        comment=None,
    ):
        try:
            self.fname = fname
            self.sname = sname
            self.email = email
            self.affiliation = affil
            self.year = year
            self.country = country
            self.city = city
            self.presentation = pres
            self.emaildist = emaildist
            self.postal = postal
            self.adress = adress
            self.sourceinfo = sourceinfo
            self.typeofreg = typeofreg
            self.comment = comment
        except ValueError as e:
            print(e)

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        if new_email == "":
            raise ValueError("Email is important!")
        elif re.search(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", new_email
        ):
            self.__email = new_email
        else:
            raise ValueError("Wrong email format!")

    @property
    def fname(self):
        return self.__fname

    @fname.setter
    def fname(self, new_fname):
        if new_fname == "":
            raise ValueError("First name is important!")
        else:
            self.__fname = new_fname

    @property
    def sname(self):
        return self.__sname

    @sname.setter
    def sname(self, new_sname):
        if new_sname == "":
            raise ValueError("Second name is important!")
        else:
            self.__sname = new_sname

    @property
    def affiliation(self):
        return self.__affiliation

    @affiliation.setter
    def affiliation(self, new_affiliation):
        if new_affiliation == "":
            raise ValueError("Affiliation is important!")
        else:
            self.__affiliation = new_affiliation

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        if new_year == "":
            raise ValueError("Year of birth is important!")
        else:
            self.__year = new_year

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, new_country):
        if new_country == "":
            raise ValueError("Country is important!")
        else:
            self.__country = new_country

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, new_city):
        if new_city == "":
            raise ValueError("City is important!")
        else:
            self.__city = new_city

    @property
    def presentation(self):
        return self.__presentation

    @presentation.setter
    def presentation(self, new_presentation):
        self.__presentation = new_presentation

    @property
    def emaildist(self):
        return self.__emaildist

    @emaildist.setter
    def emaildist(self, new_emaildist):
        self.__emaildist = new_emaildist

    @property
    def postal(self):
        return self.__postal

    @postal.setter
    def postal(self, new_postal):
        # if not re.search(r"[0-9]{6}", new_postal):
        #  raise ValueError('Wrong postal code!')
        # else:
        self.__postal = new_postal

    @property
    def adress(self):
        return self.__adress

    @adress.setter
    def adress(self, new_adress):
        self.__adress = new_adress

    @property
    def sourceinfo(self):
        return self.__sourceinfo

    @sourceinfo.setter
    def sourceinfo(self, new_sourceinfo):
        self.__sourceinfo = new_sourceinfo

    @property
    def typeofreg(self):
        return self.__typeofreg

    @typeofreg.setter
    def typeofreg(self, new_typeofreg):
        self.__typeofreg = new_typeofreg

    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, new_comment):
        self.__comment = new_comment

    def __del__(self):
        print('Registration "' + self.__email + '" deleted!!')


"""
#WRONG!!
u = Registration()
u.new('Sanya', 's', 'sanyokmail.mail', 'Sanya University', 1945, 'Piter', 'St. Peterburg', 0, False)

a = Registration()
a.new('Sanya', 'Sanin', 'sanyok@mail.mail', 'Sanya University', 1945, 'Piter', 'St. Peterburg', 0, False)
print(a.email)
"""
