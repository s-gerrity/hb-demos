"""Flask model for testing demo."""


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Employee(db.Model):
    """Employee."""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    state = db.Column(db.String(2), nullable=False, default='CA')
    dept_code = db.Column(db.String(5), db.ForeignKey('department.dept_code'))

    def __repr__(self):
        return "<Employee id=%d name=%s>" % (self.id, self.name)

    def to_dict(self):
        """Turn a employee into a dictionary.

        Useful for JSONification.

        Handles employees without departments:

            >>> leonard = Employee(name='Leonard', state='CA')
            >>> expected =  {'state': 'CA',
            ...              'id': None,
            ...              'dept_code': None,
            ...              'name': 'Leonard'}
            >>> leonard.to_dict() == expected
            True

        If the employee has a department, shows that:

            >>> legal = Department(dept_code='legal', dept='Legal', phone='555-1212')
            >>> leonard = Employee(name='Leonard', state='CA', dept=legal)
            >>> expected =  {'dept': {'dept': 'Legal', 'phone': '555-1212'},
            ...              'state': 'CA',
            ...              'id': None,
            ...              'dept_code': None,
            ...              'name': 'Leonard'}
            >>> leonard.to_dict() == expected
            True
        """

        info = {'id': self.id,
                'name': self.name,
                'state': self.state,
                'dept_code': self.dept_code,
                }
        if self.dept is not None:
            info['dept'] = {
                'dept': self.dept.dept,
                'phone': self.dept.phone,
            }
        return info

class Department(db.Model):
    """Department. A department has many employees."""

    dept_code = db.Column(db.String(5), primary_key=True)
    dept = db.Column(db.String(20), nullable=False, unique=True)
    phone = db.Column(db.String(20))

    employees = db.relationship('Employee', backref='dept')

    def __repr__(self):
        return "<Department id=%s name=%s>" % (self.dept_code, self.dept)


def example_data():
    """Create some sample data."""

    # In case this is run more than once, empty out existing data
    Employee.query.delete()
    Department.query.delete()

    # Add sample employees and departments
    df = Department(dept_code='fin', dept='Finance', phone='555-1000')
    dl = Department(dept_code='legal', dept='Legal', phone='555-2222')
    dm = Department(dept_code='mktg', dept='Marketing', phone='555-9999')

    leonard = Employee(name='Leonard', dept=dl)
    liz = Employee(name='Liz', dept=dl)
    maggie = Employee(name='Maggie', dept=dm)
    nadine = Employee(name='Nadine')

    db.session.add_all([df, dl, dm, leonard, liz, maggie, nadine])
    db.session.commit()


def connect_to_db(app, db_uri="postgresql:///empdb"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    print("Connected to DB.")
