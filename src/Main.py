from spjrud_converter import *

if __name__ == "__main__":

    db = SqlLiteDatabase('database.db')

    db.reset(['countries', 'lands', 'r', 's'])
    print(db.get_tables())

    request = {
        SelectCst(Eq('population', 65658520), Rel('countries')),
        SelectAttr(Eq('name', 'nom'), Join(Rel('countries'), Rename('name', 'nom', Rel('lands')))),
        Rename('name', 'nom',  Rel('countries')),
        Project(['name', 'country'], Rel('countries')),
        Project(['a'], Rel('r')),
        Join(Rel('r'), Rel('s')),
        Union(Rel('r'), Rel('s')),
        Diff(Rel('r'), Rel('s'))
    }

    for request in request:
        print(request)

        db.execute(request)

    db.rollback()
    db.close()
    
