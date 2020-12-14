from spjrud_converter import *

def test():
    # Tables are 'departement' and 'employe' from the question 6 in the syllabus
    db = SqlLiteDatabase('database.db')

    # db.reset(['employe', 'departement'])
    # db.create_example_table()

    # -- Uncomment these request to get the verification error --
    # SelectCst(Eq('NomDep', 'Info'), Rel('departement')), # Error attributes doesn't exist
    # Diff(Rel('departement'), Rel('employe')), # Error not the same attributes

    requests = [
        Project(['NomDept', 'Budget'], Rel('departement')), # Project
        Rename('NomDept', 'Nom', Rel('departement')), # Rename
        SelectCst(Eq('NomDept', 'Info'), Rel('departement')), # Select attribute == constant
        Join(Rel('departement'), Project(['Nom'], Rename('NomDept', 'Nom', Rel('departement')))), # Join
        SelectAttr(Eq('NomDept', 'Nom'), Join(Rel('departement'), Project(['Nom'], Rename('NomDept', 'Nom', Rel('departement'))))), # Select attribute == attribute
        Diff(Rel('departement'), SelectCst(Eq('NomDept', 'Info'), Rel('departement'))), # Difference
        Union(SelectCst(Eq('NomDept', 'Info'), Rel('departement')), SelectCst(Eq('Chef', 'E1'), Rel('departement'))), # Union

        Project(['Chef'], Join(Rename('Dept', 'NomDept', Project(['Dept'], SelectCst(Eq('NrEmp', 'E3'), Rel('employe')))), Rel('departement'))) # Question 23 in the syllabus
        ]

    # Display all request
    for x, request in enumerate(requests):
        print(f"{x} : {request}")

    # Ask the user what he want to do and execute the request
    user_response = int(input("Quelle requêtes voulez-vous executer ? "))
    if not (0 <= user_response < len(requests)):
        raise ValueError("Requête invalide.")

    print(f"\nLa requête executée est : {requests[user_response]}")
    db.execute(requests[user_response])

    # Renamme result table and show the table in the database
    db.rename(requests[user_response].name, 'result')
    print(db.get_tables())

    db.rollback()
    db.close()

def manual():
    # Tables are 'departement' and 'employe' from the question 6 in the syllabus
    db = SqlLiteDatabase('database.db')

    # --- Write your request here
    request = None

    db.execute(request)

    db.rollback()
    db.close()

if __name__ == "__main__":
    test()
    # manual()
    
