qry_create_address_tbl = """
            CREATE TABLE tblAddress (
                id text,
                country text,
                city text,
                street text,
                postal text
            )
        """

qry_create_employee_tbl = """
            CREATE TABLE tblEmployee (
                id text,
                firstName text,
                lastName text,
                phoneNumber text,
                dateOfBirth text,
                addresses text,
                title text,
                international integer,
                dateOfEmployment text
            )
        """

qry_create_trainer_tbl = """
            CREATE TABLE tblTrainer (
                id text,
                firstName text,
                lastName text,
                phoneNumber text,
                dateOfBirth text,
                addresses text,
                domain text,
                salary integer,
                courses text,
                got_raise text
            )
        """

qry_create_courses_tbl = """
            CREATE TABLE tblCourse (
                id text,
                code text,
                min integer,
                max integer
            )
        """
