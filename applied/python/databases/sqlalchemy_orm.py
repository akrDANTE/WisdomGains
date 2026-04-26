# Engine
import datetime
from sqlalchemy import create_engine, String, ForeignKey, CheckConstraint, DateTime, select, update, insert
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase, Session
from typing import List
'''
engine is the main object which sqlalchemy uses to interact with the database
it does not make connection until we call an operation which requires interaction with db
in url : sqlite-> type of db we are connecting can be MySQL, postgresql etc.
       : pysqlite-> the python DBAPI interface for interacting with the db
       : memory -> location of db -- in memory, on disk, network etc.
echo true means log all sql events to stdout.
'''
engine = create_engine(url="sqlite+pysqlite:///:memory:", echo=True)

# Doubts:
# 1. What is the need of this DeclarativeBase class?
class Base(DeclarativeBase):
       pass

# 2. What is Mapped, and mapped_column function?
# What is relationship function and how to handle relationships between the tables?
# relationship handles relationship between objects at python level and not at the db level
# foreign key handles relationship between tables at db level
class Group(Base):
    __tablename__ = "group_details"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    employees: Mapped[List["Employee"]] = relationship(back_populates="group")

    def __repr__(self):
        return f"Group(id={self.id!r}, name={self.name!r})"

class Employee(Base):
    __tablename__ = "employee_details"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True) 
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    last_name: Mapped[str] = mapped_column(String(30))
    joining_date: Mapped[datetime.datetime] = mapped_column(DateTime)
    
    # foreign key for the group
    group_id: Mapped[int] = mapped_column(ForeignKey("group_details.id"))

    # group relationship (many to one)
    group: Mapped["Group"] = relationship(back_populates="employees")


    def __repr__(self):
       return f'Employee(id={self.id}, name={self.name}, group_id={self.group_id})'
    


# generate full schema at once
Base.metadata.create_all(engine)

# create context managment using session
# insert data
with Session(engine) as session:
    group = Group(
       name = "Tech Strategy",
    )
    employee = Employee(
       name="Ghana",
       last_name="Kudo",
       joining_date = datetime.datetime(2026,2,1),
       group=group
    )
    session.add_all([group, employee])
    session.commit()

# How to perform queries?
with Session(engine) as session:
    # get all the results
    result = session.query(Employee).all()
    print(result)

    stmt = select(Employee, Group).join(Employee.group)
    result = session.execute(stmt).scalars().all()
    print(result)
    
