class Employee:
    company="Google"
    @classmethod
    def change_company(cls,new_name):
        cls.company=new_name
Employee.change_company("Microsoft")
print(Employee.company)
